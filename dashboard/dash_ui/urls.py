from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url


from . import views

# Use the views in views.py in url links to render HTML pages using the python scripts back-end

urlpatterns = [
    # commented paths are no longer in use
    #path('minimal-charts', views.index, name='index_other'),
    #path('original/<str:size_option>/<str:meeting_id>/', views.Size, name='size'),
    #path('main/<str:user_id>/<str:meeting_id>/<str:layout>/<str:size>/<str:info>/', views.Main, name='main'),
    #path('access/<str:user_id>/<str:meeting_id>/<str:layout>/<str:size>/<str:info>/', views.Access, name='access'),
    
    path('scratch/<str:user_id>/<str:layout>/<str:size>/<str:info>/', views.Scratch, name='scratch'),
    # can be used as: http://127.0.0.1:8000/dash_ui/scratch/4/0/1/1/


    
    path('test', views.testing, name='test'),
    # can be used as: http://127.0.0.1:8000/dash_ui/test

]