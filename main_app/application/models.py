from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contact(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    replied = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class StAddmissionForm(models.Model):
    af_id = models.AutoField(primary_key=True)
    af_name = models.CharField(max_length=100)
    af_dob = models.DateField()
    af_gender = models.CharField(max_length=11)
    af_email = models.CharField(max_length=30)
    af_phone_no = models.IntegerField()
    af_community_catogery = models.CharField(db_column='af_community/catogery', max_length=15)  # Field renamed to remove unsuitable characters.
    af_adhar_card = models.CharField(max_length=200)
    af_caste_certificate = models.CharField(max_length=200)
    af_migration_certificate = models.CharField(max_length=200)
    af_marks_last_sem = models.IntegerField()
    af_gpa = models.IntegerField()
    af_marksheets = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'st_addmission_form'


class StCollageRegistration(models.Model):
    cr_id = models.AutoField(primary_key=True, db_comment='id of collage_registration.')
    cr_name = models.CharField(max_length=50, blank=True, null=True, db_comment='name of collage.')
    cr_location = models.CharField(max_length=200, blank=True, null=True, db_comment='location of collage.')
    cr_email = models.CharField(max_length=50, blank=True, null=True)
    cr_phone_no = models.IntegerField()
    documents = models.CharField(max_length=200)
    cr_programs = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'st_collage_registration'


class StStudentRegistration(models.Model):
    sr_id = models.AutoField(primary_key=True, db_comment='id of student registration.')
    sr_username = models.CharField(max_length=20, blank=True, null=True, db_comment='username of student.')
    sr_call_number = models.IntegerField(blank=True, null=True, db_comment='contact number of student.')
    sr_gmail = models.CharField(max_length=20, blank=True, null=True, db_comment='gmail of student.')
    sr_password = models.CharField(max_length=20, blank=True, null=True, db_comment='password of this registration.')
    sr_confirm_password = models.CharField(max_length=20, blank=True, null=True, db_comment='confirm password.')

    class Meta:
        managed = False
        db_table = 'st_student_registration'


class StTransferForm(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_s_name = models.CharField(max_length=100, blank=True, null=True)
    t_dob = models.DateField(db_column='t_DOB', blank=True, null=True, db_comment='date of birth')  # Field name made lowercase.
    t_gender = models.CharField(max_length=10, blank=True, null=True, db_comment='gender of student')
    t_email = models.CharField(max_length=50, blank=True, null=True)
    t_phone_no = models.IntegerField(blank=True, null=True, db_comment='phone number of student')
    t_address = models.CharField(max_length=100)
    t_present_college = models.CharField(max_length=50, blank=True, null=True, db_comment="student's present_collage ")
    t_future_college = models.CharField(max_length=50, blank=True, null=True, db_comment='future collage where student want to go.')
    t_reason_for_transfer = models.CharField(max_length=500, blank=True, null=True, db_comment='t_reason_for_transfer.')
    t_present_course = models.CharField(max_length=30, blank=True, null=True, db_comment='present course of student.')
    t_community_category = models.CharField(db_column='t_community/category', max_length=30, blank=True, null=True, db_comment='cart of student.')  # Field renamed to remove unsuitable characters.
    t_aadhar_card = models.FileField(max_length=200, blank=True, null=True, db_comment='aadhar card of student.')
    t_caste_certificate = models.FileField(max_length=30, blank=True, null=True)
    t_migration_certificate = models.FileField(max_length=30, blank=True, null=True, db_comment='migration_certificate.')
    t_marks_last_sem = models.IntegerField(blank=True, null=True, db_comment='marks of last sam.')
    st_marksheets = models.FileField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_transfer_form'
