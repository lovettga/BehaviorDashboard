from django.shortcuts import render
from .get_info import *
from .models import *
import gviz_api

# Create your views here.

# NEW COMMENT HERE

# View for the test_database.html
#######################################################
def testing(request):
    display_table = HDisplaytable.objects.all()
    talk_stream = HTalkdatastream.objects.all()
    all_users = HUsers.objects.all()

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company
    pie_options = ['100', 'percentage', 'selection', '15']
    bar_options = ['#CCC', 'out', 'selection', '10', 'black']


    talk_data = []
    overlap_data = []
    backchannel_data = []
    emotion_data = 1

    user_colors = []
    #for i in range(len(all_users)):
    #    user_colors.append((all_users[i].username, all_colors[i]))

    for i in range(len(display_table)):
        #user_colors.append((all_users[i].username, all_colors[i]))

        row = display_table[i]
        user_name = row.user_id.username
        talktime = row.talktime
        overlaps = row.overlaps
        backchannels = row.backchannels
        emotion = row.emotion

        user_colors.append((user_name, all_colors[i]))

        talk_data.append((user_name, talktime))
        overlap_data.append((user_name, overlaps, all_colors[i]))
        backchannel_data.append((user_name, backchannels, all_colors[i]))
        
        if user_name == all_users[0].username:
            emotion_data = emotion


    context = {'display_table': display_table, 'talk_stream': talk_stream, 'user_colors': user_colors, 'all_colors': all_colors,\
        'pie_options': pie_options, 'bar_options': bar_options,\
        'talk_data': talk_data, 'overlap_data': overlap_data, 'backchannel_data': backchannel_data, 'emotion_data': emotion_data}
    return render(request, 'test_database.html', context)

#######################################################

# View for scratch.html
#######################################################
def Scratch(request, user_id, layout, size, info):
    user_profile = HUsers.objects.get(user_id=user_id)
    display_table = HDisplaytable.objects.all()
    rapport_table = HRapport.objects.all()
    all_users = HUsers.objects.all()

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company

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

    talk_data = []
    overlap_data = []
    backchannel_data = []
    emotion_data = 1

    user_colors = []
    #for i in range(len(all_users)):
    #    user_colors.append((all_users[i].username, all_colors[i]))

    ################
    new_display_table = []
    
    # put current user at the front of the display table data
    for i in range(len(display_table)):
        row_user_id = display_table[i].user_id
        if row_user_id.user_id == user_profile.user_id:
            new_display_table.append(display_table[i])
    for i in range(len(display_table)):
        row_user_id = display_table[i].user_id
        if row_user_id.user_id != user_profile.user_id:
            new_display_table.append(display_table[i])

    ################



    for i in range(len(new_display_table)):
        #user_colors.append((all_users[i].username, all_colors[i]))

        row = new_display_table[i]
        user_name = row.user_id.username
        talktime = row.talktime
        overlaps = row.overlaps
        backchannels = row.backchannels
        emotion = row.emotion

        user_colors.append((user_name, all_colors[i]))

        talk_data.append((user_name, talktime))
        overlap_data.append((user_name, overlaps, all_colors[i]))
        backchannel_data.append((user_name, backchannels, all_colors[i]))
        
        if user_name == all_users[0].username:
            emotion_data = emotion


    interaction_data = []
    interaction_colors = []
    # add the current user color first
    interaction_colors.append(user_colors[0][1])
    for i in range(len(rapport_table)):
        first_user = rapport_table[i].primary_user
        other_user = rapport_table[i].secondary_user
        value = rapport_table[i].rapport

        # if the first person in the interaction is the current user
        if first_user.user_id == user_profile.user_id:
            interaction_data.append((user_profile.username, other_user.username, int(value)))
            for j in range(len(user_colors)):
                if other_user.username == user_colors[j][0]:
                    interaction_colors.append(user_colors[j][1])

    # sankey_data = [['Person 1', 'Person 2', 6], ['Person 1', 'Person 3', 2], ['Person 1', 'Person 4', 8]]


    context = {'size': size, 'layout': layout, 'info': info, 'user_profile': user_profile, 'user_colors': user_colors,\
        'all_colors': all_colors, 'pie_options': pie_options, ' bar_options': bar_options, 'sankey_options': sankey_options,\
        'settings_font': settings_font, 'talk_data': talk_data, 'overlap_data': overlap_data, 'backchannel_data': backchannel_data, \
        'interaction_data': interaction_data, 'emotion_data': emotion_data,\
        'interaction_colors': interaction_colors}
 

    # GET RID OF MEETING OBJECT

    return render(request, 'scratch.html', context) 
