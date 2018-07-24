# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contacts(models.Model):
    cid = models.AutoField(primary_key=True)
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    fax = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class EssProductService(models.Model):
    product_service_id = models.IntegerField(primary_key=True)
    prefix = models.ForeignKey('EssProductServiceTopLevel', models.DO_NOTHING, db_column='prefix', blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ess_product_service'


class EssProductServiceTopLevel(models.Model):
    prefix_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ess_product_service_top_level'


class GeocodedSample(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geocoded_sample'


class GeocodedSample1(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geocoded_sample_1'


class IconGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icon_groups'


class IdsTest(models.Model):
    id = models.TextField(blank=True, null=True)
    oid = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    branch_name = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ids_test'


class IdsTest2(models.Model):
    id = models.TextField(primary_key=True)
    oid = models.IntegerField()
    bid = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    branch_name = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ids_test_2'


class IdsTesttest(models.Model):
    uid = models.TextField(primary_key=True)
    oid = models.IntegerField()
    bid = models.IntegerField()
    hqname = models.TextField(blank=True, null=True)
    branch_name = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ids_testtest'


class Locations(models.Model):
    lid = models.AutoField(primary_key=True)
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid', blank=True, null=True)
    primary_loc = models.NullBooleanField()
    location_name = models.CharField(max_length=-1, blank=True, null=True)
    comments = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    address2 = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    county = models.CharField(max_length=-1, blank=True, null=True)
    country = models.CharField(max_length=-1, blank=True, null=True)
    match_addr = models.CharField(max_length=-1, blank=True, null=True)
    side = models.CharField(max_length=-1, blank=True, null=True)
    ref_id = models.CharField(max_length=-1, blank=True, null=True)
    geographic_location = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'locations'


class NaicsIndustries(models.Model):
    naics_id = models.IntegerField(primary_key=True)
    naics_sector = models.ForeignKey('NaicsSectors', models.DO_NOTHING, blank=True, null=True)
    industry_name = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naics_industries'


class NaicsIndustryAsocOrg(models.Model):
    naics = models.ForeignKey(NaicsIndustries, models.DO_NOTHING)
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'naics_industry_asoc_org'
        unique_together = (('oid', 'naics'),)


class NaicsSectors(models.Model):
    naics_sector_id = models.IntegerField(primary_key=True)
    sector_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naics_sectors'


class OrgAndTypeAssoc(models.Model):
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid', primary_key=True)
    tid = models.ForeignKey('Types', models.DO_NOTHING, db_column='tid')

    class Meta:
        managed = False
        db_table = 'org_and_type_assoc'
        unique_together = (('oid', 'tid'),)


class OrgToEssProductInput(models.Model):
    product_service = models.ForeignKey(EssProductService, models.DO_NOTHING, primary_key=True)
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid')

    class Meta:
        managed = False
        db_table = 'org_to_ess_product_input'
        unique_together = (('product_service', 'oid'),)


class OrgToEssProductOutput(models.Model):
    product_service = models.ForeignKey(EssProductService, models.DO_NOTHING, primary_key=True)
    oid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='oid')

    class Meta:
        managed = False
        db_table = 'org_to_ess_product_output'
        unique_together = (('product_service', 'oid'),)


class Organizations(models.Model):
    oid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    source = models.CharField(max_length=-1, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=-1, blank=True, null=True)
    ally = models.BooleanField()
    defunct = models.BooleanField()
    hide_from_site = models.BooleanField()
    icon_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class PaOrgsChildcareTmp(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    type_name = models.CharField(max_length=-1, blank=True, null=True)
    location_name = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    address2 = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    geographic_location = models.TextField(blank=True, null=True)  # This field type is a guess.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_orgs_childcare_tmp'


class PaOrgsTmp(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    type_name = models.CharField(max_length=-1, blank=True, null=True)
    location_name = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    address2 = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    geographic_location = models.TextField(blank=True, null=True)  # This field type is a guess.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_orgs_tmp'


class PanelData(models.Model):
    uid = models.TextField()
    oid = models.IntegerField()
    bid = models.IntegerField()
    hqname = models.TextField()
    branch_name = models.TextField()
    comments = models.TextField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    contact_email = models.TextField(blank=True, null=True)
    externaldatareference = models.TextField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    number_5digit_zip = models.DecimalField(db_column='5digit_zip', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4digit_zip_field = models.DecimalField(db_column='4digit_zip ', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panel_data'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Suggestions(models.Model):
    organization = models.ForeignKey(Organizations, models.DO_NOTHING, blank=True, null=True)
    original_organization_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    submitter_name = models.CharField(max_length=255, blank=True, null=True)
    submitter_email = models.CharField(max_length=255, blank=True, null=True)
    ally = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suggestions'


class SurveyMain(models.Model):
    uid = models.TextField(primary_key=True)
    oid = models.IntegerField()
    bid = models.IntegerField()
    id = models.IntegerField(blank=True, null=True)
    surv_id = models.IntegerField(blank=True, null=True)
    surv_section = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    surv_admin = models.CharField(max_length=10, blank=True, null=True)
    surv_origin = models.CharField(max_length=10, blank=True, null=True)
    v1 = models.CharField(max_length=20, blank=True, null=True)
    v5 = models.CharField(max_length=20, blank=True, null=True)
    v8 = models.DateTimeField(blank=True, null=True)
    v9 = models.DateTimeField(blank=True, null=True)
    v10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_consent = models.NullBooleanField()
    q2_name = models.CharField(max_length=30, blank=True, null=True)
    q2_add1 = models.CharField(max_length=30, blank=True, null=True)
    q2_city = models.CharField(max_length=15, blank=True, null=True)
    q2_state = models.CharField(max_length=2, blank=True, null=True)
    q2_zip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_phone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_email = models.CharField(max_length=20, blank=True, null=True)
    q2_web = models.CharField(max_length=20, blank=True, null=True)
    q2_contact = models.CharField(max_length=30, blank=True, null=True)
    q2_title = models.CharField(max_length=10, blank=True, null=True)
    q2_phone2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_email2 = models.CharField(max_length=20, blank=True, null=True)
    q2_add2 = models.CharField(max_length=30, blank=True, null=True)
    q2_add2_det = models.TextField(blank=True, null=True)
    q2_add3 = models.CharField(max_length=30, blank=True, null=True)
    q2_add3_det = models.TextField(blank=True, null=True)
    q3_consumer = models.NullBooleanField()
    q3_buying = models.NullBooleanField()
    q3_vollunteer_cons = models.NullBooleanField()
    q3_housing = models.NullBooleanField()
    q3_clt = models.NullBooleanField()
    q3_1_6 = models.NullBooleanField()
    q3_worker = models.NullBooleanField()
    q3_producer = models.NullBooleanField()
    q3_volunteer_prod = models.NullBooleanField()
    q3_garden = models.NullBooleanField()
    q3_selfemployed = models.NullBooleanField()
    q3_carework = models.NullBooleanField()
    q3_cu = models.NullBooleanField()
    q3_cdcu = models.NullBooleanField()
    q3_lending = models.NullBooleanField()
    q3_mutual = models.NullBooleanField()
    q3_3_5 = models.NullBooleanField()
    q3_3_6 = models.NullBooleanField()
    q3_fair_trade = models.NullBooleanField()
    q3_csa = models.NullBooleanField()
    q3_currency = models.NullBooleanField()
    q3_time_bank = models.NullBooleanField()
    q3_barter = models.NullBooleanField()
    q3_4_6 = models.NullBooleanField()
    q3_budgeting = models.NullBooleanField()
    q3_resources = models.NullBooleanField()
    q3_5_3 = models.NullBooleanField()
    q3_5_4 = models.NullBooleanField()
    q3_5_5 = models.NullBooleanField()
    q3_5_6 = models.NullBooleanField()
    q4_other = models.TextField(blank=True, null=True)
    q5_product1 = models.CharField(max_length=20, blank=True, null=True)
    q5_product2 = models.CharField(max_length=20, blank=True, null=True)
    q5_product3 = models.CharField(max_length=20, blank=True, null=True)
    q6_input1 = models.CharField(max_length=20, blank=True, null=True)
    q6_input2 = models.CharField(max_length=20, blank=True, null=True)
    q6_input3 = models.CharField(max_length=20, blank=True, null=True)
    q7_sic_naics = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_description = models.TextField(blank=True, null=True)
    q8_consent = models.NullBooleanField()
    q9_established = models.SmallIntegerField(blank=True, null=True)
    q10_type = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    q10_type_other = models.TextField(blank=True, null=True)
    q11_ownership = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q11_ownership_other = models.TextField(blank=True, null=True)
    q12_nonmbrwrkrs = models.NullBooleanField()
    q13_ind_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q13_mbr_orgs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q14_payroll = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q15_inc_benefit = models.NullBooleanField()
    q16_benefits = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q17_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q18_ftime_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q18_ptime_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q18_volunteer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q19_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q20_wrkr_residence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q20_wrkr_residence_other = models.TextField(blank=True, null=True)
    q21_black_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_black_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_white_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_white_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_latino_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_latino_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_asian_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_asian_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_other_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q21_other_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q22_black = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q22_white = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q22_latino = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q22_asian = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q22_other = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_women_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_women_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_lgbt_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_lgbt_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_disab_wrkr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q23_disab_mbr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q24_women = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q24_lgbt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q24_disab = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q25_area_served = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q25_area_served_other = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q26_input_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q26_input_area_other = models.TextField(blank=True, null=True)
    q27 = models.NullBooleanField()
    latitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    longitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    accuracy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_main'


class Test1(models.Model):
    type = models.TextField(blank=True, null=True)
    form = models.CharField(max_length=-1, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    zip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test1'


class Test3(models.Model):
    n = models.CharField(max_length=50, blank=True, null=True)
    v = models.CharField(max_length=6, blank=True, null=True)
    a = models.CharField(max_length=100, blank=True, null=True)
    b = models.CharField(max_length=100, blank=True, null=True)
    c = models.CharField(max_length=20, blank=True, null=True)
    s = models.CharField(max_length=2, blank=True, null=True)
    z = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test3'


class Types(models.Model):
    tid = models.AutoField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    password_digest = models.CharField(max_length=255, blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
