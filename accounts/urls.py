from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/', views.signout, name='signout'),
    path('settings/', views.editprofile, name='accountsettings'),
    path('deleteaccount/', views.deleteaccount, name='deleteaccount'),
    path('resetimage/', views.resetimage, name='resetimage'),
    path('creatorsignup/', views.creatorsignup, name='creatorsignup'),
    path('creatorinfo/', views.creatorinfo, name='creatorinfo'),
    path('userdashboard/', views.dashboard, name='dashboard'),
    path('uploadcontent/', views.uploadcontent, name='uploadcontent'),
    path('createtvpack/', views.uploadtvpack, name='uploadtvpack'),
    path('createmusicpack/', views.uploadmusicpack, name='uploadmusicpack'),
    path('createpodcastpack/', views.uploadpodcastpack, name='uploadpodcastpack'),
    path('uploadsrc/', views.uploadsrc, name='uploadsrc'),
    path('creatordashboard/', views.creatordashboard, name='creatordashboard'),
]