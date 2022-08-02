from django.shortcuts import render
import random
from rest_framework.response import Response
from rest_framework import generics,status
from .models import *
from django.views.decorators.cache import cache_page
from .serializers import *

@cache_page(60*15)
def podcasthome(request):
    popularitems = PodcastPack.objects.all().order_by('-likes')[:5]
    recentuploads = PodcastPack.objects.all().order_by('-uploaded_date')
    podcastitems = list(PodcastPack.objects.all())
    featuredpodcasts = random.sample(podcastitems, 3)
    return render(request, 'podcast-home.html',{'popularitems':popularitems,'recentuploads':recentuploads,'featuredpodcasts':featuredpodcasts})

def podcastsingle(request,id):
    podcast = PodcastPack.objects.get(id=id)
    podcastitems = PodcastRepo.objects.filter(podcastpack=podcast)
    return render(request, 'podcast-single.html', {'podcast': podcast,'podcastitems': podcastitems})

def like(request,id):
    single = PodcastPack.objects.get(id=id)
    single.likes += 1
    single.save()
    user = request.user
    like = UserPodcastLike(music=single,user =user)
    like.save()
    podcastsingle(request, id)

def dislike(request,id):
    single = PodcastPack.objects.get(id=id)
    single.likes -= 1
    single.save()
    user = request.user
    like = UserPodcastLike(album=single,user =user)
    like.save()
    podcastsingle(request, id)

def podcastsearch(request):
    popularitems = PodcastPack.objects.all().order_by('-likes')[:5]
    podcastitems = list(PodcastPack.objects.all())
    featuredpodcasts = random.sample(podcastitems, 3)
    try:
        term = request.POST['search']
        result = PodcastPack.objects.filter(name=term)
        return render(request, 'podcast-search.html', {'result':result,'popularitems':popularitems,'featuredpodcasts':featuredpodcasts})
    except PodcastPack.DoesNotExist:
        return render(request, 'oops.html')

#Podcastsearch API to search for a podcast
class Podcastsearch(generics.ListAPIView):
    serializer_class = PodcastSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        return PodcastPack.objects.filter(name=name)

#Podcastlike API to submit a like/dislike for a podcast
class PodcastLike(generics.UpdateAPIView):
    serializer_class = PodcastSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return PodcastPack.objects.get(id=id)

#Podcastdetail API to return the details of a podcast
class PodcastDetail(generics.ListAPIView):
    serializer_class = PodcastSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return PodcastPack.objects.get(id=id)

#PodcastList API to return all podcasts in a users favorites list
class PodcastList(generics.ListAPIView):
    serializer_class = PodcastListSerializer
    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserPodcastList.objects.filter(user=user)

#PodcastList API to return all podcasts in a users liked podcast list
class PodcastLikeList(generics.ListAPIView):
    serializer_class = PodcastLikeSerializer
    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserPodcastLike.objects.filter(user=user)