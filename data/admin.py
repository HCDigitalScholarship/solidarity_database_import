from django.contrib.gis import admin
#from django.contrib import admin
from data.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export import widgets
from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    raw_id_fields = ("oid",)
    def get_oid(self, obj): #For foreign key
        return obj.oid.oid
    get_oid.admin_order_field = 'oid' #Allows column order sorting
    get_oid.short_description = 'OID' #Renames column head
admin.site.register(Contacts, ContactsAdmin)


class EssProductServiceAdmin(admin.ModelAdmin):
    list_display = ('product_service_id', 'get_prefix', 'name')
    search_fields = ['product_service_id', 'prefix__prefix_id', 'name']
    list_filter = ['prefix__prefix_id']
    raw_id_fields = ("prefix",)

    def get_prefix(self, obj):
        return obj.prefix.prefix_id
    get_prefix.admin_order_field = 'prefix'
    get_prefix.short_description = 'PREFIX'
admin.site.register(EssProductService, EssProductServiceAdmin)


class EssProductServiceTopLevelAdmin(admin.ModelAdmin):
    list_display = ('prefix_id', 'name')
    search_fields = ['prefix_id', 'name']
admin.site.register(EssProductServiceTopLevel, EssProductServiceTopLevelAdmin)


class IconGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['id', 'name']
admin.site.register(IconGroups, IconGroupsAdmin)


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
    raw_id_fields = ("oid",)
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
        #credit_union_oid_list = list(OrgAndTypeAssoc.objects.filter(tid = 15).values_list('oid', flat = True))
        ncua_oid_list = list(NCUA.objects.all().values_list('oid', flat = True))
        # have proven:
        # Locations.objects.all() == self.Meta.model.objects.all()
        # NCUA = self.Meta.model.objects.filter(oid__oid__in = ncua_oid_list)
        for deleted_row in self.Meta.model.objects.filter(oid__oid__in = ncua_oid_list).exclude(pk__in=self.imported_rows_pks):
            result.deleted_rows.append(deleted_row)
        result.deleted_rows_count = len(result.deleted_rows)
        self.Meta.model.objects.filter(oid__oid__in = ncua_oid_list).exclude(pk__in=self.imported_rows_pks).delete()
        resources.ModelResource.after_import(self, dataset, result, using_transactions, dry_run, **kwargs)

class CreditUnionsAdmin(ImportExportModelAdmin):
    resource_class = CreditUnionsResource
    list_display = ('lid', 'get_oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location')
    search_fields = ['lid','oid__oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id']
    raw_id_fields = ("oid",)
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


class NCUAResource(resources.ModelResource):
    class Meta:
        model = NCUA
        fields = ['oid']
        import_id_fields = ['oid']

class NCUAAdmin(ImportExportModelAdmin):
    resource_class = NCUAResource
    list_display = ('oid', 'get_tid')
    actions = ['delete_all']

    def get_tid(self, obj):
        try:
            return OrgAndTypeAssoc.objects.filter(oid = obj.oid).values_list('tid', flat = True)[0]
        except IndexError:
            return "No tid"
    get_tid.admin_order_field = 'oid'
    get_tid.short_description = 'TID'

    def delete_all(self, request, queryset):
        NCUA.objects.all().delete()
        '''
        TODO:
        if 'apply' in request.POST:
            print ('I am here!')
            NCUA.objects.all().delete()
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'admin/data/delete_intermediate.html', context={'opts': NCUA._meta})
        '''
    delete_all.short_description = 'Delete all NCUA'
admin.site.register(NCUA, NCUAAdmin)


class NCUA_editResource(resources.ModelResource):
    class Meta:
        model = NCUA_edit
        fields = ['lid', 'oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location']
        import_id_fields = ['address']

    def before_import_row(self, row, **kwargs):
        if row['oid'] == '' or None:
            try:
                row['oid'] = Locations.objects.filter(address__iexact = row['address'], state__iexact = row['state']).values_list('oid', flat = True)[0]
            except IndexError:
                pass

class NCUA_editAdmin(ImportExportModelAdmin):
    resource_class = NCUA_editResource
    list_display = ('lid', 'oid', 'address', 'address2', 'city', 'state', 'zipcode', 'county', 'country', 'match_addr', 'side', 'ref_id', 'geographic_location')
admin.site.register(NCUA_edit, NCUA_editAdmin)


class NaicsIndustriesAdmin(admin.ModelAdmin):
    list_display = ('naics_id', 'get_naics_sector', 'industry_name')
    search_fields = ['naics_id', 'naics_sector__naics_sector_id', 'industry_name']
    list_filter = ['naics_sector__naics_sector_id']
    raw_id_fields = ("naics_sector",)

    def get_naics_sector(self, obj):
        return obj.naics_sector.naics_sector_id
    get_naics_sector.admin_order_field = 'naics_sector'
    get_naics_sector.short_description = 'NAICS SECTOR'
admin.site.register(NaicsIndustries, NaicsIndustriesAdmin)


class NaicsIndustryAsocOrgAdmin(admin.ModelAdmin):
    list_display = ('get_naics', 'get_oid')
    search_fields = ['naics__naics_id', 'oid__oid']
    raw_id_fields = ("naics", "oid")

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'

    def get_naics(self, obj):
        return obj.naics.naics_id
    get_naics.admin_order_field = 'naics'
    get_naics.short_description = 'NAICS'
admin.site.register(NaicsIndustryAsocOrg, NaicsIndustryAsocOrgAdmin)


class NaicsSectorsAdmin(admin.ModelAdmin):
    list_display = ('naics_sector_id', 'sector_name')
    search_fields = ['naics_sector_id', 'sector_name']
admin.site.register(NaicsSectors, NaicsSectorsAdmin)


class OrgAndTypeAssocAdmin(admin.ModelAdmin):
    list_display = ('get_oid', 'get_tid')
    search_fields = ['oid__oid', 'tid__tid']
    list_filter = ['tid__tid']
    raw_id_fields = ("oid",)

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'

    def get_tid(self, obj):
        return obj.tid.tid
    get_tid.admin_order_field = 'tid'
    get_tid.short_description = 'TID'
admin.site.register(OrgAndTypeAssoc, OrgAndTypeAssocAdmin)


class OrgToEssProductInputAdmin(admin.ModelAdmin):
    list_display = ('get_product_service', 'get_oid')
    search_fields = ['get_product_service__product_service_id', 'oid__oid']
    raw_id_fields = ("product_service", "oid")

    def get_product_service(self, obj):
        return obj.product_service.product_service_id
    get_product_service.admin_order_field = 'product_service'
    get_product_service.short_description = 'PRODUCT SERVICE'

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'
admin.site.register(OrgToEssProductInput, OrgToEssProductInputAdmin)


class OrgToEssProductOutputAdmin(admin.ModelAdmin):
    list_display = ('get_product_service', 'get_oid')
    search_fields = ['get_product_service__product_service_id', 'oid__oid']
    raw_id_fields = ("product_service", "oid")

    def get_product_service(self, obj):
        return obj.product_service.product_service_id
    get_product_service.admin_order_field = 'product_service'
    get_product_service.short_description = 'PRODUCT SERVICE'

    def get_oid(self, obj):
        return obj.oid.oid
    get_oid.admin_order_field = 'oid'
    get_oid.short_description = 'OID'
admin.site.register(OrgToEssProductOutput, OrgToEssProductOutputAdmin)


class PaOrgsChildcareTmpAdmin(admin.ModelAdmin):
    pass
#admin.site.register(PaOrgsChildcareTmp, PaOrgsChildcareTmpAdmin)


class PaOrgsTmpAdmin(admin.ModelAdmin):
    pass
#admin.site.register(PaOrgsTmp, PaOrgsTmpAdmin)


class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ('get_oid', 'original_organization_id', 'created_at', 'updated_at', 'submitter_name', 'submitter_email', 'ally')
    search_fields = ['organization__oid', 'original_organization_id', 'created_at', 'updated_at', 'submitter_name', 'submitter_email', 'ally']
    raw_id_fields = ("organization",)

    def get_oid(self, obj):
        return obj.organization.oid
    get_oid.admin_order_field = 'organization'
    get_oid.short_description = 'ORGANIZATION ID'
admin.site.register(Suggestions, SuggestionsAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ('tid', 'type_name')
admin.site.register(Types, TypesAdmin)
