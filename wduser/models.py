# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WduserAuthuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.IntegerField()
    date_joined = models.DateTimeField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.IntegerField()
    role_type = models.PositiveIntegerField()
    nickname = models.CharField(max_length=64, blank=True, null=True)
    headimg = models.CharField(max_length=200, blank=True, null=True)
    active_code = models.CharField(max_length=20, blank=True, null=True)
    active_code_valid = models.IntegerField()
    remark = models.CharField(max_length=400, blank=True, null=True)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    dedicated_link = models.CharField(max_length=60, blank=True, null=True)
    age_id = models.IntegerField(blank=True, null=True)
    seniority_id = models.IntegerField(blank=True, null=True)
    gender_id = models.IntegerField(blank=True, null=True)
    marriage_id = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    rank_id = models.IntegerField(blank=True, null=True)
    sequence_id = models.IntegerField(blank=True, null=True)
    politics_id = models.IntegerField(blank=True, null=True)
    education_id = models.IntegerField(blank=True, null=True)
    importlot = models.IntegerField(blank=True, null=True)
    profile = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wduser_authuser'


class WduserOrg(models.Model):
    account_name = models.CharField(max_length=30, blank=True, null=True)
    org_level1 = models.CharField(max_length=150, blank=True, null=True)
    org_level2 = models.CharField(max_length=150, blank=True, null=True)
    org_level3 = models.CharField(max_length=150, blank=True, null=True)
    org_level4 = models.CharField(max_length=150, blank=True, null=True)
    org_level5 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wduser_org'