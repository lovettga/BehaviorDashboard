from django.db import models

# Create your models here.
# py manage.py inspectdb > models.py 
# ^^ USE THIS TO GET THE UPDATED MODELS.PY FROM THE DASHABORD DATABASE
# by copying the line into the terminal, this will update the OTHER models.py under dashboard
# copy and paste the desired models here for use in views.py


class HDisplaytable(models.Model):
    displaytable_iterator_key = models.AutoField(primary_key=True)
    user_id = models.OneToOneField('HUsers', models.DO_NOTHING, db_column='display_ID')  # Field name made lowercase.
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
    user_id = models.ForeignKey('HUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_key_test_table'


class HTalkdatastream(models.Model):
    talkdatastream_iterator_key = models.AutoField(primary_key=True)
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='talkdatastream_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_talkdatastream'


class HTalkdatastreambackup(models.Model):
    talkdatastreambackup_iterator_key = models.AutoField(primary_key=True)
    counter = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='talkdatastreambackup_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_talkdatastreambackup'


class HUsers(models.Model):
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_users'

class HRapport(models.Model):
    rapport_iterator_key = models.AutoField(primary_key=True)
    primary_user = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='primary_user_ID', related_name="primary")  # Field name made lowercase.
    secondary_user = models.ForeignKey('HUsers', models.DO_NOTHING, db_column='secondary_user_ID',  related_name="secondary")  # Field name made lowercase.
    rapport = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_rapport'


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
