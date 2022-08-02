from django.shortcuts import render
import random
from rest_framework.response import Response
from rest_framework import status,viewsets,generics
from .models import *
from django.views.decorators.cache import cache_page
from accounts.models import *
from .serializers import *

@cache_page(60*15)
def musichome(request):
    popularitems = MusicPack.objects.all().order_by('-likes')[:5]
    recentuploads = MusicPack.objects.all().order_by('-uploaded_date')
    musicitems = list(MusicPack.objects.filter(type='album'))
    featuredalbums = random.sample(musicitems, 3)
    musicitems2 = list(MusicPack.objects.filter(type='single'))
    featuredsingles = random.sample(musicitems2, 3)
    return render(request, 'music-home.html',{'popularitems':popularitems,'recentuploads':recentuploads,'featuredalbums':featuredalbums,'featuredsingles':featuredsingles})

def musicsingle(request,id):
    single = MusicPack.objects.get(id=id)
    items = MusicRepo.objects.filter(musicpack=single)
    return render(request, 'music-single.html',{'single':single,'items':items})


def like(request,id):
    single = MusicPack.objects.get(id=id)
    single.likes += 1
    single.save()
    user = request.user
    like = UserMusicLike(music=single,user =user)
    like.save()
    musicsingle(request, id)

def dislike(request,id):
    single = MusicPack.objects.get(id=id)
    single.likes -= 1
    single.save()
    user = request.user
    like = UserMusicLike(album=single,user =user)
    like.save()
    musicsingle(request, id)


def musicsearch(request):
    popularitems = MusicPack.objects.all().order_by('-likes')[:5]
    musicitems = list(MusicPack.objects.filter(type='album'))
    featuredalbums = random.sample(musicitems, 3)
    musicitems2 = list(MusicPack.objects.filter(type='single'))
    featuredsingles = random.sample(musicitems2, 3)
    term = request.POST['search']
    try:
        result = MusicPack.objects.filter(name=term)
        return render(request, 'music-search.html',
                      {'result': result, 'popularitems': popularitems, 'featuredalbums': featuredalbums,
                       'featuredsingles': featuredsingles})
    except MusicPack.DoesNotExist:
        return render(request, 'oops.html')


# Musicsearch API to search for a music object
class Musicsearch(generics.ListAPIView):
    serializer_class = MusicSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return MusicPack.objects.filter(name=name)


# Musiclike API to submit a like/dislike for a music object
class MusicLike(generics.UpdateAPIView):
    serializer_class = MusicSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return MusicPack.objects.filter(id=id)


# Musicdetail API to return the details of a music object
class MusicDetail(generics.ListAPIView):
    serializer_class = MusicSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return MusicPack.objects.filter(id=id)

#MusicList API to return all music objects in a users favorites list
class MusicList(generics.ListAPIView):
    serializer_class = MusicListSerializer
    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserMusicList.objects.filter(user=user)

#MusicList API to return all music objects in a users liked list
class MusicLikeList(generics.ListAPIView):
    serializer_class = MusicLikeSerializer

    def get_queryset(self):
        user = User.objects.get(name=self.kwargs['name'])
        return UserMusicLike.objects.filter(user=user)

