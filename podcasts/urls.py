from django.urls import path
from . import views

urlpatterns = [
    path('podcasthome/', views.podcasthome, name='podcasthome'),
    path('podcastsingle/<str:id>', views.podcastsingle, name='podcastsingle'),
    path('like/<str:id>', views.like, name='podcastlike'),
    path('podcastsearch/', views.podcastsearch, name='podcastsearch'),
    path('dislike/<str:id>', views.dislike, name='podcastdislike'),
]