from django.contrib.gis import admin
#from django.contrib import admin
from data.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export import widgets
from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import messages

from data.geocode import google
from django.contrib.gis.geos import Point

from data.myresults import myResult #to customize Result class from import_export

# Register your models here.
class OrganizationsResource(resources.ModelResource):
    class Meta:
        model = Organizations
        import_id_fields = ['oid']

class OrganizationsAdmin(ImportExportModelAdmin):
    resource_class = OrganizationsResource
    list_display = ('oid', 'name', 'website', 'description', 'source', 'year_founded', 'notes', 'ally', 'defunct', 'hide_from_site', 'icon_group_id')
    search_fields = ['oid', 'name', 'website', 'description', 'source', 'year_founded', 'notes', 'ally', 'defunct', 'hide_from_site', 'icon_group_id']
admin.site.register(Organizations, OrganizationsAdmin)


#Foreign Key Widget
class OidWidget(widgets.ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        return self.model.objects.get_or_create(oid = value)[0]


class ContactsResource(resources.ModelResource):
    oid = fields.Field(column_name='oid', attribute='oid', widget=OidWidget(Organizations, 'oid'))
    class Meta:
        model = Contacts
        fields = ['cid', 'oid', 'name', 'title', 'phone', 'fax', 'email', 'uid']
        import_id_fields = ['oid']

class ContactsAdmin(ImportExportModelAdmin):
    resource_class = ContactsResource
    list_display = ('cid', 'get_oid', 'name', 'title', 'phone', 'fax', 'email', 'uid')
    search_fields = ['cid', 'oid__oid', 'name', 'title', 'phone', 'fax', 'email', 'uid']
    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'
admin.site.register(Contacts, ContactsAdmin)


class LocationsResource(resources.ModelResource):
    oid = fields.Field(column_name='oid', attribute='oid', widget=OidWidget(Organizations, 'oid'))
    class Meta:
        model = Locations
        fields = ['address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location']
        import_id_fields = ['oid', 'address']
        skip_unchanged = True

    def skip_row(self, instance, original):
        '''
        to determine whether the newly imported object is different from the already present object and if therefore the given row should be skipped or not
        '''
        if not self._meta.skip_unchanged:
            return False
        # when the original doesn't have a value in the geographic_location, this row shouldn't be skipped
        if original.geographic_location == '':
            return False
        for field in self.get_import_fields()[:-1]:
        # notes for [:-1] --if the original has a value in geographic_location and its address is same as the instance's, no new geocoding is needed and this row should be skipped
            try:
                # For fields that are models.fields.related.ManyRelatedManager
                # we need to compare the results
                if list(field.get_value(instance).all()) != list(field.get_value(original).all()):
                    return False
            except AttributeError:
                if field.get_value(instance) != field.get_value(original):
                    if field.get_value(instance) == '' and field.get_value(original) == None: # in the old db, empty attributes are stored as None
                        continue
                    else:
                        return False
        return True

    def before_save_instance(self, instance, using_transactions, dry_run): #if the current row is not to be skipped
        full_address = instance.address + " " + instance.address2 + " " + instance.city + " " + instance.state + " " + instance.zipcode + " " + instance.county + " " + instance.country
        geocode_result = google(full_address)
        if len(geocode_result) != 0: #for the cases when addresses are not provided
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            instance.geographic_location = Point(x=lng, y=lat, srid=4326)

class LocationsAdmin(ImportExportModelAdmin): #(admin.ModelAdmin ):
    resource_class = LocationsResource
    list_display = ('lid', 'get_oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location')
    search_fields = ['lid','oid__oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id']
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'
admin.site.register(Locations, LocationsAdmin)


class CreditUnionsResource(resources.ModelResource):
    oid = fields.Field(column_name='oid', attribute='oid', widget=OidWidget(Organizations, 'oid'))
    imported_rows_pks = []
    class Meta:
        model = Locations
        fields = ['address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location']
        import_id_fields = ['oid', 'address']
        skip_unchanged = True

    @classmethod
    def get_result_class(self):
        ''' to customize the Result class '''
        return myResult

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        self.imported_rows_pks = []

    def skip_row(self, instance, original):
        if not self._meta.skip_unchanged:
            return False
        if original.geographic_location == '':
            return False
        for field in self.get_import_fields()[:-1]:
            try:
                if list(field.get_value(instance).all()) != list(field.get_value(original).all()):
                    return False
            except AttributeError:
                if field.get_value(instance) != field.get_value(original):
                    if field.get_value(instance) == '' and field.get_value(original) == None:
                        continue
                    else:
                        return False
        self.imported_rows_pks.append(instance.pk)
        return True

    def before_save_instance(self, instance, using_transactions, dry_run): #if the current row is not to be skipped
        full_address = instance.address + " " + instance.address2 + " " + instance.city + " " + instance.state + " " + instance.zipcode + " " + instance.county + " " + instance.country
        geocode_result = google(full_address)
        if len(geocode_result) != 0: #for the cases when addresses are not provided
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            instance.geographic_location = Point(x=lng, y=lat, srid=4326)

    def after_save_instance(self, instance, using_transactions, dry_run):
        self.imported_rows_pks.append(instance.pk)

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        credit_union_oid_list = list(OrgAndTypeAssoc.objects.filter(tid = 15).values_list('oid', flat = True))
        # have proven:
        # Locations.objects.all() == self.Meta.model.objects.all()
        # credit_union = self.Meta.model.objects.filter(oid__oid__in = credit_union_oid_list)
        for deleted_row in self.Meta.model.objects.filter(oid__oid__in = credit_union_oid_list).exclude(pk__in=self.imported_rows_pks):
            result.deleted_rows.append(deleted_row)
        result.deleted_rows_count = len(result.deleted_rows)
        print (result.deleted_rows_count)
        self.Meta.model.objects.filter(oid__oid__in = credit_union_oid_list).exclude(pk__in=self.imported_rows_pks).delete()
        resources.ModelResource.after_import(self, dataset, result, using_transactions, dry_run, **kwargs)

class CreditUnionsAdmin(ImportExportModelAdmin):
    resource_class = CreditUnionsResource
    list_display = ('lid', 'get_oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location')
    search_fields = ['lid','oid__oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id']
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'

    class Meta:
        proxy = True
admin.site.register(CreditUnions, CreditUnionsAdmin)


class OrgAndTypeAssocAdmin(admin.ModelAdmin):
    list_display = ('get_oid', 'get_tid')
    search_fields = ['oid__oid', 'tid__tid']

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'

    def get_tid(self, obj):
        return obj.tid.tid
    get_tid.admin_order_field = 'tid'
    get_tid.short_description = 'TID'
admin.site.register(OrgAndTypeAssoc, OrgAndTypeAssocAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ('tid', 'type_name')
admin.site.register(Types, TypesAdmin)
