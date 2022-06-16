from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url


from . import views

urlpatterns = [
    path('minimal-charts', views.index, name='index_other'),
    # path('<str:room_name>/', views.room, name='room'),

    path('original/<str:size_option>/<str:meeting_id>/', views.Size, name='size'),
    path('main/<str:user_id>/<str:meeting_id>/<str:layout>/<str:size>/<str:info>/', views.Main, name='main'),
    path('access/<str:user_id>/<str:meeting_id>/<str:layout>/<str:size>/<str:info>/', views.Access, name='access'),
    path('scratch/<str:user_id>/<str:meeting_id>/<str:layout>/<str:size>/<str:info>/', views.Scratch, name='scratch'),
]