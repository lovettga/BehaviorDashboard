from django.shortcuts import render
from .get_info import *
from .models import *
import gviz_api

# Create your views here.

# View for the test_database.html
#######################################################
def testing(request):
    # the following 3 lines grab all instances of the models below in the form of a list
    display_table = HDisplaytable.objects.all()
    talk_stream = HTalkdatastream.objects.all()
    all_users = HUsers.objects.all()

    # these are prespecified colors and chart options that are used in the html
    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']  
    pie_options = ['100', 'percentage', 'selection', '15']
    bar_options = ['#CCC', 'out', 'selection', '10', 'black']

    # initialize the data lists for use in the charts
    talk_data = []
    overlap_data = []
    backchannel_data = []
    emotion_data = 1
    user_colors = []

    # loop through the display table to gather information such as talktime, overlaps, backchannels, and emotion
    for i in range(len(display_table)):
        #user_colors.append((all_users[i].username, all_colors[i]))

        # denote the current row
        row = display_table[i]
        # the subscripts that hold the information are found in models.py (dash_ui)
        # for example: user_id points to the HUsers that the row is referencing, and the username holds the name of the HUsers
        user_name = row.user_id.username
        talktime = row.talktime
        overlaps = row.overlaps
        backchannels = row.backchannels
        emotion = row.emotion

        # this links the user with a specific color for chart displays
        user_colors.append((user_name, all_colors[i]))

        # appends the data to the correct data list for chart displays
        talk_data.append((user_name, talktime))
        overlap_data.append((user_name, overlaps, all_colors[i]))
        backchannel_data.append((user_name, backchannels, all_colors[i]))
        
        # grabs only the emotion data for the current user
        if user_name == all_users[0].username:
            emotion_data = emotion

    # each 'variable': view_variable contains the variable that can be used in the html
    # which gets it's information from the view_variable above
    # (I kept them the same for simplicity and smoothness between the views and the html)
    context = {'display_table': display_table, 'talk_stream': talk_stream, 'user_colors': user_colors, 'all_colors': all_colors,\
        'pie_options': pie_options, 'bar_options': bar_options,\
        'talk_data': talk_data, 'overlap_data': overlap_data, 'backchannel_data': backchannel_data, 'emotion_data': emotion_data}

    # this view renders the test_database.html document with the context included above
    return render(request, 'test_database.html', context)

#######################################################

# View for scratch.html
#######################################################
# the "user_id" "layout" "size" and "info" come from the url that is entered
# in http://127.0.0.1:8000/dash_ui/scratch/4/0/1/1/ --> user_id=4, layout=0, size=1, info=1
def Scratch(request, user_id, layout, size, info):
    # identifies and grabs the user profile from HUsers based on the provided user_id in the url
    user_profile = HUsers.objects.get(user_id=user_id)
    # the other tables below hold all instances of the models
    display_table = HDisplaytable.objects.all()
    rapport_table = HRapport.objects.all()
    all_users = HUsers.objects.all()

    # hex color denotions of the display colors
    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f'] 

    ####      INFO OPTIONS    ####
    # initialize all options
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

    # initialize data lists
    talk_data = []
    overlap_data = []
    backchannel_data = []
    emotion_data = 1
    user_colors = []

    ################
    # rearrange the order of people within the display table, putting the current user first
    new_display_table = []
    
    # put current user at the front of the display table data
    for i in range(len(display_table)):
        row_user_id = display_table[i].user_id
        # if the row being looked at is the current user's row
        if row_user_id.user_id == user_profile.user_id:
            new_display_table.append(display_table[i])
    # append the rest of the users' rows to the new display table list
    for i in range(len(display_table)):
        row_user_id = display_table[i].user_id
        # if the row being looked at is NOT the current user's row
        if row_user_id.user_id != user_profile.user_id:
            new_display_table.append(display_table[i])

    ################

    # loop through the new display table to sort data
    for i in range(len(new_display_table)):
        # determine current row
        row = new_display_table[i]
        # the subscripts that hold the information are found in models.py (dash_ui)
        # for example: user_id points to the HUsers that the row is referencing, and the username holds the name of the HUsers
        user_name = row.user_id.username
        talktime = row.talktime
        overlaps = row.overlaps
        backchannels = row.backchannels
        emotion = row.emotion

        # assigns each color to the users
        user_colors.append((user_name, all_colors[i]))

        # add the data to the data lists for display
        talk_data.append((user_name, talktime))
        overlap_data.append((user_name, overlaps, all_colors[i]))
        backchannel_data.append((user_name, backchannels, all_colors[i]))
        
        # only grab the emotion data for the current user
        if row.user_id.user_id == user_profile.user_id:
            emotion_data = emotion

    # rapport data collection uses a different table than the display table
    #initialize the data sorting for the rapport
    interaction_data = []
    interaction_colors = []
    # add the current user color first
    interaction_colors.append(user_colors[0][1])
    # loop throught the rapport table
    for i in range(len(rapport_table)):
        # determine the primary user (one person in the interaction)
        # and the secondary user (the other person in the interaction)
        first_user = rapport_table[i].primary_user
        other_user = rapport_table[i].secondary_user
        # grab rapport value for the interaction
        value = rapport_table[i].rapport

        # if the first/ primary person in the interaction is the current user
        if first_user.user_id == user_profile.user_id:
            # add the interaction to the current user's interaction data
            interaction_data.append((user_profile.username, other_user.username, int(value)))
            # also update the interaction colors list
            for j in range(len(user_colors)):
                if other_user.username == user_colors[j][0]:
                    interaction_colors.append(user_colors[j][1])

    # this is purely test data to ensure the sankey table is operating correctly (this just shows the template needed for the rapport table)
    # sankey_data = [['Person 1', 'Person 2', 6], ['Person 1', 'Person 3', 2], ['Person 1', 'Person 4', 8]]

    # each 'variable': view_variable contains the variable that can be used in the html
    # which gets it's information from the view_variable above
    # (I kept them the same for simplicity and smoothness between the views and the html)
    context = {'size': size, 'layout': layout, 'info': info, 'user_profile': user_profile, 'user_colors': user_colors,\
        'all_colors': all_colors, 'pie_options': pie_options, ' bar_options': bar_options, 'sankey_options': sankey_options,\
        'settings_font': settings_font, 'talk_data': talk_data, 'overlap_data': overlap_data, 'backchannel_data': backchannel_data, \
        'interaction_data': interaction_data, 'emotion_data': emotion_data,\
        'interaction_colors': interaction_colors}

    # this view renders the scratch.html document with the context included above
    return render(request, 'scratch.html', context) 
