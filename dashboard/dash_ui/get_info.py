from .models import *

def get_participants(meeting_id):
    meeting_object = Meeting.objects.get(id=meeting_id)
    all_participants = meeting_object.participants.all()

    return all_participants


def get_all_users():
    all_users = DashUser.objects.all()
    return all_users


# put data in a json format for google charts
def get_json_data(input_list):
    pass
