from django.urls import path
from . import views

urlpatterns = [
    path('musichome/', views.musichome, name='musichome'),
    path('musicsingle/<str:id>', views.musicsingle, name='musicsingle'),
    path('like/<str:id>', views.like, name='like'),
    path('musicsearch/', views.musicsearch, name='musicsearch'),
    path('dislike/<str:id>', views.dislike, name='dislike'),
]