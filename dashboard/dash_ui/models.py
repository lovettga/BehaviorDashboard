from django.db import models

# Create your models here.
# py manage.py inspectdb > models.py 
# ^^ USE THIS TO GET THE UPDATED MODELS.PY FROM THE DASHABORD DATABASE

class Users(models.Model):
    username = models.CharField(db_column='Username', 
                                max_length=50, 
                                blank=True, 
                                null=True)  # Field name made lowercase.
    user_id = models.AutoField(db_column='User_ID', 
                               primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

class Talkstream(models.Model):
    dd_primary = models.AutoField(db_column='DD_Primary', primary_key=True)  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    dd_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='DD_User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talkstream'

class TalkstreamCondensed(models.Model):
    dd_con_key = models.AutoField(db_column='DD_Con_Key', primary_key=True)  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    dd_con = models.OneToOneField('Users', models.DO_NOTHING, db_column='DD_Con_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talkstream_condensed'

class KeyTestTable(models.Model):
    key_test_primary = models.AutoField(primary_key=True)
    other = models.IntegerField(blank=True, null=True)
    key_test_link = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_test_table'

##################################################################

# MODELS FROM SQLITE

#class DashUser(models.Model):
#    username = models.CharField(max_length=80)
#    password = models.CharField(max_length=80)
#    first_name = models.CharField(max_length=80)
#    last_name = models.CharField(max_length=80)

#    def __str__(self):
#        return "{} {}".format(self.first_name, self.last_name)

#class Meeting(models.Model):
#    title = models.CharField(max_length=80)
#    date = models.DateField()
#    participants = models.ManyToManyField(DashUser,
#                                     blank=True)
####################################################################



#class ActiveMeeting(models.Model):
#    meeting = models.ForeignKey(Meeting, 
#                               on_delete=models.CASCADE,
#                               blank=True,
#                               null=True)
#    user = models.ForeignKey(DashUser, 
#                               on_delete=models.CASCADE,
#                               blank=True,
#                               null=True)
#    talk_time = models.IntegerField()
#    overlaps = models.IntegerField()
#    back_channels = models.IntegerField()
#    emotion = models.IntegerField()
