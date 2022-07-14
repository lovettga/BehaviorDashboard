from django.shortcuts import render
from .get_info import *
import gviz_api

# Create your views here.

# on first load 
def index(request):
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
    #new_data = [('Work', 11), ('Eat', 2), ('Commute', 2), ('Watching TV', 2), ('Sleeping', 7)]
    new_data = [('Person 1', 20.3), ('Person 2', 11.4), ('Person 3', 5.3), ('Person 4', 15), ('Person 5', 7)]

    # all_colors = ['blue', 'red', 'orange', 'purple', 'green', 'yellow']  #STARTING COLORS
    # all_colors = ['#d6a2ad', '#c3b59f', '#a0af84', '#4a6670']            #Floral
    # all_colors = ['#3a405a', '#aec5eb', '#e9afa3', '#685044']            #Buisness Casual
    # all_colors = ['#8edce6', '#a7b0ca', '#725e54', '#443627']            #Fairy Bark
    # all_colors = ['#f6bd60', '#f5cac3', '#84a59d', '#f28482']            #Bright Floral
    # all_colors = ['#ffadad', '#ffd6a5', '#caffbf', '#9bf6ff', '#bdb2ff'] #Pastels
    # all_colors = ['#8cb369', '#f4a259', '#5b8e7d', '#bc4b51']            #Neutrals

    # all_colors = ['#49ADD5', '#cd797d', '#FFC233', '#83AFA0', '#9B75BD']   #Light-Company
    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company
    # all_colors = ['#004966', '#95373C', '#B88100', '#487063', '#5E3C7C']   #Dark-Company


    user_colors = []    # ['Person', 'blue']
    bar_style = []      # ['Person', 5, 'gray']
    for i in range(len(new_data)):
        user_colors.append((new_data[i][0], all_colors[i]))
        bar_style.append((new_data[i][0], new_data[i][1], all_colors[i]))

    # ('Person 1', 'Person 2', 6)
    sankey_data = [('Person 1', 'Person 2', 6), ('Person 1', 'Person 3', 2), ('Person 1', 'Person 4', 8), ('Person 2', 'Person 1', 6), ('Person 2', 'Person 3', 13), ('Person 1', 'Person 5', 0)]

    context = {'data': data, 'new_data': new_data, 'user_colors': user_colors, 'bar_style': bar_style,
        'sankey_data': sankey_data, 'all_colors': all_colors}

    return render(request, 'index_other.html', context)
    # return render(request, 'dashboard/classrooms_settings.html', context)


def Size(request, size_option, meeting_id):
    meeting_object = Meeting.objects.get(id=meeting_id)
    participant_list = get_participants(meeting_id)
    user_list = get_all_users()

    all_meetings = Meeting.objects.all()

    # minimal chart things #####
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
    #new_data = [('Work', 11), ('Eat', 2), ('Commute', 2), ('Watching TV', 2), ('Sleeping', 7)]
    new_data = [('Person 1', 20.3), ('Person 2', 11.4), ('Person 3', 5.3), ('Person 4', 15), ('Person 5', 7)]

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company

    user_colors = []    # ['Person', 'blue']
    bar_style = []      # ['Person', 5, 'gray']
    for i in range(len(new_data)):
        user_colors.append((new_data[i][0], all_colors[i]))
        bar_style.append((new_data[i][0], new_data[i][1], all_colors[i]))

    # ('Person 1', 'Person 2', 6)
    sankey_data = [('Person 1', 'Person 2', 6), ('Person 1', 'Person 3', 2), ('Person 1', 'Person 4', 8), ('Person 2', 'Person 1', 6), ('Person 2', 'Person 3', 13), ('Person 1', 'Person 5', 0)]


    #############################



    context = {'participant_list': participant_list, 'user_list': user_list, 'size_option': size_option,\
        'meeting_object': meeting_object, 'all_meetings': all_meetings, 'data': data, 'new_data': new_data,\
        'user_colors': user_colors, 'bar_style': bar_style, 'sankey_data': sankey_data, 'all_colors': all_colors}

    return render(request, 'index.html', context)


def Main(request, user_id, meeting_id, layout, size, info):
    meeting_object = Meeting.objects.get(id=meeting_id)
    participant_list = get_participants(meeting_id)
    user_object = DashUser.objects.get(id=user_id)
    user_list = get_all_users()

    all_meetings = Meeting.objects.all()

    ######### chart things #######
    
    new_data = [('Person 1', 20.3), ('Person 2', 11.4), ('Person 3', 5.3), ('Person 4', 15), ('Person 5', 7)]

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company

    user_colors = []    # ['Person', 'blue']
    bar_style = []      # ['Person', 5, 'gray']
    for i in range(len(new_data)):
        user_colors.append((new_data[i][0], all_colors[i]))
        bar_style.append((new_data[i][0], new_data[i][1], all_colors[i]))

    sankey_data = [('Person 1', 'Person 2', 6), ('Person 1', 'Person 3', 2), ('Person 1', 'Person 4', 8), ('Person 2', 'Person 1', 6), ('Person 2', 'Person 3', 13), ('Person 1', 'Person 5', 0)]
    ##############################

    # ensure first user in participant list is the current user
    new_participant_list = [user_object]
    for participant in participant_list:
        if participant.id is not user_object.id:
            new_participant_list.append(participant)

    user_colors = []    # ['Person', 'blue']
    for i in range(len(new_participant_list)):
        user_colors.append((new_participant_list[i], all_colors[i]))

    participant_num = len(new_participant_list)

    ##############################

    count = 1
    # Talk time data
    talk_data = []
    for participant in new_participant_list:
        talk_data.append((participant, count))
        count += 1

    count = 2
    # Overlap data
    overlap_data = []
    for i in range(len(new_participant_list)):
        overlap_data.append((new_participant_list[i], count, all_colors[i]))
        count += 2

    count = 3
    # Back channels data
    back_data = []
    for i in range(len(new_participant_list)):
        back_data.append((new_participant_list[i], count, all_colors[i]))
        count += 3

    # Emotion data
    emotion_level = 4

    count = 1
    # Interactions data
    interaction_data = []
    for participant in new_participant_list:
        if participant.id is not user_object.id:
            interaction_data.append((user_object, participant, int(count)))
            count += 2




    ##############################


    context = {'participant_list': new_participant_list, 'user_list': user_list, 'size': size, 'layout': layout,\
        'meeting_object': meeting_object, 'all_meetings': all_meetings, 'new_data': new_data,\
        'user_colors': user_colors, 'bar_style': bar_style, 'sankey_data': sankey_data, 'all_colors': all_colors,\
        'user_profile': user_object, 'participant_num': participant_num, \
        'talk_data': talk_data, 'overlap_data': overlap_data, 'back_data': back_data, 'emotion_level': emotion_level, 'interaction_data':interaction_data}

    return render(request, 'main_display.html', context)    


def Access(request, user_id, meeting_id, layout, size, info):
    meeting_object = Meeting.objects.get(id=meeting_id)
    participant_list = get_participants(meeting_id)
    user_object = DashUser.objects.get(id=user_id)
    user_list = get_all_users()

    all_meetings = Meeting.objects.all()

    ######### chart things #######
    
    new_data = [('Person 1', 20.3), ('Person 2', 11.4), ('Person 3', 5.3), ('Person 4', 15), ('Person 5', 7)]

    # all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company
    all_colors = ['#f5793a', '#a95aa1', '#85c0f9', '#0f2080', '#006050']  # Color blind palette

    user_colors = []    # ['Person', 'blue']
    bar_style = []      # ['Person', 5, 'gray']
    for i in range(len(new_data)):
        user_colors.append((new_data[i][0], all_colors[i]))
        bar_style.append((new_data[i][0], new_data[i][1], all_colors[i]))

    sankey_data = [('Person 1', 'Person 2', 6), ('Person 1', 'Person 3', 2), ('Person 1', 'Person 4', 8), ('Person 2', 'Person 1', 6), ('Person 2', 'Person 3', 13), ('Person 1', 'Person 5', 0)]
    ##############################

    # ensure first user in participant list is the current user
    new_participant_list = [user_object]
    for participant in participant_list:
        if participant.id is not user_object.id:
            new_participant_list.append(participant)

    user_colors = []    # ['Person', 'blue']
    for i in range(len(new_participant_list)):
        user_colors.append((new_participant_list[i], all_colors[i]))

    participant_num = len(new_participant_list)

    ##############################

    count = 1
    # Talk time data
    talk_data = []
    for participant in new_participant_list:
        talk_data.append((participant, count))
        count += 1

    count = 2
    # Overlap data
    overlap_data = []
    for i in range(len(new_participant_list)):
        overlap_data.append((new_participant_list[i], count, all_colors[i]))
        count += 2

    count = 3
    # Back channels data
    back_data = []
    for i in range(len(new_participant_list)):
        back_data.append((new_participant_list[i], count, all_colors[i]))
        count += 3

    # Emotion data
    emotion_level = 4 * 10

    count = 1
    # Interactions data
    interaction_data = []
    for participant in new_participant_list:
        if participant.id is not user_object.id:
            interaction_data.append((user_object, participant, int(count)))
            count += 2
    ##############################

    ####      INFO OPTIONS    ####

    pie_options = []
    bar_options = []
    sankey_options = []
    # small text
    if info == '1':
        pie_options = ['100', 'percentage', 'selection', '10']
        bar_options = ['#CCC', 'out', 'selection', '10', 'black']
        sankey_options = ['true', 10]
        settings_font = 14
    # large text
    elif info == '2':
        pie_options = ['100', 'percentage', 'selection', '14']
        bar_options = ['#CCC', 'out', 'selection', '14', 'black']
        sankey_options = ['true', 14]
        settings_font = 16
    # no text
    else:
        pie_options = ['100', 'none', 'none', '10']
        bar_options = ['transparent', 'none', 'none', '10', 'transparent']
        sankey_options = ['true', 10]
        settings_font = 14

    ###############################


    context = {'participant_list': new_participant_list, 'user_list': user_list, 'size': size, 'layout': layout,\
        'meeting_object': meeting_object, 'all_meetings': all_meetings, 'new_data': new_data, 'info': info,\
        'user_colors': user_colors, 'bar_style': bar_style, 'sankey_data': sankey_data, 'all_colors': all_colors,\
        'user_profile': user_object, 'participant_num': participant_num, \
        'talk_data': talk_data, 'overlap_data': overlap_data, 'back_data': back_data, 'emotion_level': emotion_level,\
        'interaction_data':interaction_data, 'pie_options': pie_options, 'bar_options': bar_options,\
        'sankey_options': sankey_options, 'settings_font': settings_font}

    return render(request, 'accessibility.html', context)        












def Scratch(request, user_id, meeting_id, layout, size, info):
    meeting_object = Meeting.objects.get(id=meeting_id)
    participant_list = get_participants(meeting_id)
    user_object = DashUser.objects.get(id=user_id)
    user_list = get_all_users()

    all_meetings = Meeting.objects.all()

    ######### chart things #######
    
    new_data = [('Person 1', 20.3), ('Person 2', 11.4), ('Person 3', 5.3), ('Person 4', 15), ('Person 5', 7)]

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company

    user_colors = []    # ['Person', 'blue']
    bar_style = []      # ['Person', 5, 'gray']
    for i in range(len(new_data)):
        user_colors.append((new_data[i][0], all_colors[i]))
        bar_style.append((new_data[i][0], new_data[i][1], all_colors[i]))

    sankey_data = [('Person 1', 'Person 2', 6), ('Person 1', 'Person 3', 2), ('Person 1', 'Person 4', 8), ('Person 2', 'Person 1', 6), ('Person 2', 'Person 3', 13), ('Person 1', 'Person 5', 0)]
    
    ##############################

    # ensure first user in participant list is the current user
    new_participant_list = [user_object]
    for participant in participant_list:
        if participant.id is not user_object.id:
            new_participant_list.append(participant)

    user_colors = []    # ['Person', 'blue']
    for i in range(len(new_participant_list)):
        user_colors.append((new_participant_list[i], all_colors[i]))

    participant_num = len(new_participant_list)

    ####### Data Configure ############

    count = 1
    # Talk time data
    talk_data = []
    for participant in new_participant_list:
        talk_data.append((participant, count))
        count += 1

    count = 2
    # Overlap data
    overlap_data = []
    for i in range(len(new_participant_list)):
        overlap_data.append((new_participant_list[i], count, all_colors[i]))
        count += 2

    count = 3
    # Back channels data
    back_data = []
    for i in range(len(new_participant_list)):
        back_data.append((new_participant_list[i], count, all_colors[i]))
        count += 3

    # Emotion data
    emotion_level = 4 * 10

    count = 1
    # Interactions data
    interaction_data = []
    for participant in new_participant_list:
        if participant.id is not user_object.id:
            interaction_data.append((user_object, participant, int(count)))
            count += 2

    ##############################


    ####      INFO OPTIONS    ####

    pie_options = []
    bar_options = []
    sankey_options = []
    # small text
    if info == '1':
        pie_options = ['100', 'percentage', 'selection', '10']
        bar_options = ['#CCC', 'out', 'selection', '10', 'black']
        sankey_options = ['true', 10]
        settings_font = 14
    # large text
    elif info == '2':
        pie_options = ['100', 'percentage', 'selection', '14']
        bar_options = ['#CCC', 'out', 'selection', '14', 'black']
        sankey_options = ['true', 14]
        settings_font = 16
    # no text
    else:
        pie_options = ['100', 'none', 'none', '10']
        bar_options = ['transparent', 'none', 'none', '10', 'transparent']
        sankey_options = ['true', 10]
        settings_font = 14

    ###############################


    context = {'participant_list': new_participant_list, 'user_list': user_list, 'size': size, 'layout': layout,\
        'info': info, 'meeting_object': meeting_object, 'all_meetings': all_meetings, 'new_data': new_data,\
        'user_colors': user_colors, 'bar_style': bar_style, 'sankey_data': sankey_data, 'all_colors': all_colors,\
        'user_profile': user_object, 'participant_num': participant_num, \
        'talk_data': talk_data, 'overlap_data': overlap_data, 'back_data': back_data, 'emotion_level': emotion_level, 'interaction_data':interaction_data,\
        'pie_options': pie_options, 'bar_options': bar_options, 'sankey_options': sankey_options, 'settings_font': settings_font }

    return render(request, 'scratch.html', context) 



#def TEST():
#    result = test_database()
#    return render(request, test_database.html)