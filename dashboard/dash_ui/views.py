from django.shortcuts import render
from .get_info import *
from .models import *
import gviz_api

# Create your views here.

#######################################################
def testing(request):
    display_table = HDisplaytable.objects.all()
    talk_stream = HTalkdatastream.objects.all()


    context = {'display_table': display_table, 'talk_stream': talk_stream}
    return render(request, 'test_database.html', context)

"""
def testing(request):
    all_users = HUsers.objects.all()
    all_data = HTalkdatastream.objects.all()
    key_table = HKeyTestTable.objects.all()
    cond_data = HTalktime.objects.all()
    display = HDisplaytable.objects.all()

    all_colors = ['#006992', '#bc4b51', '#eca400', '#5b8e7d', '#784c9f']   #Neutral-Company
    pie_options = ['100', 'percentage', 'selection', '15']
    bar_options = ['#CCC', 'out', 'selection', '10', 'black']

    user_colors = []
    for i in range(len(all_users)):
        user_colors.append((all_users[i].username, all_colors[i]))

    talk_data = []
    overlap_data = []
    for i in range(len(key_table)):
        pair = key_table[i]
        participant = pair.key_test_link.username
        value = pair.other
        talk_data.append((participant, value))
        overlap_data.append((participant, value, all_colors[i]))

    cond_talk_data = []
    for i in range(len(cond_data)):
        curr_row = cond_data[i]
        participant = curr_row.dd_con.username
        value = curr_row.counter
        cond_talk_data.append((participant, value))

    context = {'all_users': all_users, 'all_data': all_data, 'key_table': key_table, 'all_colors': all_colors,\
        'pie_options': pie_options, 'bar_options': bar_options, 'talk_data': talk_data, 'overlap_data': overlap_data,\
            'cond_data': cond_data, 'cond_talk_data': cond_talk_data, 'user_colors':user_colors, 'display': display}
    return render(request, 'test_database.html', context)
"""
#######################################################

