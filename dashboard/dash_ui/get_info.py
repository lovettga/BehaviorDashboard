from .models import *
#import mysql.connector

#db = mysql.connector.connect(host="100.64.0.26", user="Gabby", passwd="12345",
#                             database="testdatabase")

#mycursor = db.cursor()


def get_participants(meeting_id):
    meeting_object = Meeting.objects.get(id=meeting_id)
    all_participants = meeting_object.participants.all()

    return all_participants


def get_all_users():
    all_users = DashUser.objects.all()
    return all_users


# put data in a json format for google charts
#def test_database():
#    mycursor.execute("SELECT * FROM users")
#    for x in mycursor:
#        print(x)
