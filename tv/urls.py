from django.urls import path
from . import views

urlpatterns = [
    path('tvhome/', views.tvhome, name='tvhome'),
    path('tvsingle/<str:id>', views.tvsingle, name='tvsingle'),
    path('stream/<str:id>', views.tvstream, name='tvstream'),
    path('like/<str:id>', views.like, name='tvlike'),
    path('tvsearch/', views.tvsearch, name='tvsearch'),
    path('dislike/<str:id>', views.dislike, name='tvdislike'),
]