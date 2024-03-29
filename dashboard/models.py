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


class HDisplaytable(models.Model):
    displaytable_iterator_key = models.AutoField(primary_key=True)
    display = models.OneToOneField('HUsers', models.DO_NOTHING, db_column='display_ID')  # Field name made lowercase.
    talktime = models.IntegerField(blank=True, null=True)
    overlaps = models.IntegerField(blank=True, null=True)
    backchannels = models.IntegerField(blank=True, null=True)
    emotion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_displaytable'


class HKeyTestTable(models.Model):
    key_test_primary = models.AutoField(primary_key=True)
    other = models.IntegerField(blank=True, null=True)
    key_test_link = models.ForeignKey('HUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_key_test_table'


class HRapport(models.Model):
    rapport_iterator_key = models.AutoField(primary_key=True)
    primary_user = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='primary_user_ID')  # Field name made lowercase.
    secondary_user = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='secondary_user_ID')  # Field name made lowercase.
    rapport = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_rapport'


class HTalkdatastream(models.Model):
    talkdatastream_iterator_key = models.AutoField(primary_key=True)
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    talkdatastream = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='talkdatastream_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_talkdatastream'


class HTalkdatastreambackup(models.Model):
    talkdatastreambackup_iterator_key = models.AutoField(primary_key=True)
    counter = models.IntegerField(blank=True, null=True)
    talkdatastreambackup = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='talkdatastreambackup_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_talkdatastreambackup'


class HUsers(models.Model):
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_users'
