from django.db import models

# Create your models here.

class DashUser(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Meeting(models.Model):
    title = models.CharField(max_length=80)
    date = models.DateField()
    participants = models.ManyToManyField(DashUser,
                                     blank=True)
    
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
