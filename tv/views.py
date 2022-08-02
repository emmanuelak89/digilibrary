from django.shortcuts import render
import random
from rest_framework import status,viewsets,generics
from .models import *
from django.views.decorators.cache import cache_page
from .serializers import *

#@cache_page(60*15)
def tvhome(request):
    popularitems = VideoPack.objects.all().order_by('-likes')[:5]
    recentuploads = reversed(VideoPack.objects.all().order_by('-uploaded_date'))
    movies = list(VideoPack.objects.filter(type='movie'))
    featuredmovies = random.sample(movies, 3)
    series = list(VideoPack.objects.filter(type='series'))
    featuredseries = random.sample(series, 3)
    return render(request, 'tv-home.html',{'popularitems':popularitems,'recentuploads':recentuploads,'featuredmovies':featuredmovies,'featuredseries':featuredseries})

def tvsingle(request,id):
    movie = VideoPack.objects.get(id=id)
    video = VideoRepo.objects.filter(videopack=movie)
    return render(request, 'tv-single.html', {'movie': movie,'video':video})

def tvstream(request,id):
    video = VideoRepo.objects.get(id=id)
    pack = VideoRepo.objects.filter(videopack=video.videopack)
    return render(request, 'tv-stream.html', {'video':video,'pack':pack})



def like(request,id):
    single = VideoPack.objects.get(id=id)
    single.likes += 1
    single.save()
    user = request.user
    like = UserVideoLike(music=single,user =user)
    like.save()
    tvsingle(request, id)

def dislike(request,id):
    single = VideoPack.objects.get(id=id)
    single.likes -= 1
    single.save()
    user = request.user
    like = UserVideoLike(album=single,user =user)
    like.save()
    tvsingle(request, id)

def tvsearch(request):
    popularitems = VideoPack.objects.all().order_by('-likes')[:5]
    movies = list(VideoPack.objects.filter(type='movie'))
    featuredmovies = random.sample(movies, 3)
    series = list(VideoPack.objects.filter(type='series'))
    featuredseries = random.sample(series, 3)
    try:
        term = request.POST['search']
        result = VideoPack.objects.filter(name=term)
        return render(request, 'tv-search.html', {'result':result,'popularitems':popularitems,'featuredmovies':featuredmovies,'featuredseries':featuredseries})
    except VideoPack.DoesNotExist:
        return render(request, 'oops.html')

# Videosearch API to search for a Video object
class Videosearch(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return VideoPack.objects.filter(name=name)


# Videolike API to submit a like/dislike for a Video object
class VideoLike(generics.UpdateAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return VideoPack.objects.filter(id=id)


# Videodetail API to return the details of a Video object
class VideoDetail(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return VideoPack.objects.filter(id=id)

#VideoList API to return all Video objects in a users favorites list
class MusicList(generics.ListAPIView):
    serializer_class = VideoListSerializer
    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserVideoList.objects.filter(user=user)

#VideoList API to return all Video objects in a users liked list
class MusicLikeList(generics.ListAPIView):
    serializer_class = VideoLikeSerializer

    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserVideoLike.objects.filter(user=user)




