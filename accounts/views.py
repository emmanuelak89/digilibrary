from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from .models import *
from tv.models import *
from music.models import *
from podcasts.models import *
import random
from rest_framework.response import Response
from rest_framework import generics,status
from django.views.decorators.cache import cache_page
from .serializers import BioSerializer

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['username']
        image = request.FILES['image']
        fs = FileSystemStorage()
        doc = fs.save(image.name, image)
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            u = User.objects.get(username=email)
            bio = Bio(user=u, name =name,image=doc,role='user')
            bio.save()
            auth.login(request, user)
            return redirect('dashboard')
        else:
            mg = 'passwords must match'
            return render(request, 'signup.html', {'mg': mg})
    else:
        return render(request, 'signup.html')


def creatorsignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        bio = request.POST['bio']
        image = request.FILES['image']
        fs = FileSystemStorage()
        doc = fs.save(image.name, image)
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            u = User.objects.get(username=email)
            creator = Bio(user=u, name =name,image=doc,role='creator',bio=bio)
            creator.save()
            auth.login(request, user)
            return redirect('creatordashboard')
        else:
            mg = 'passwords must match'
            return render(request, 'signup.html', {'mg': mg})
    else:
        return render(request, 'csignup.html')

def signin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            userbio = Bio.objects.get(email=user)
            if userbio.role == 'user':
                return redirect('dashboard')
            else:
                return redirect('creatordashboard')
        else:
            return render(request, 'signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('home')

def dashboard(request):
    try:
        liked = UserMusicLike.objects.filter(user=request.user).count()+UserVideoLike.objects.filter(user=request.user).count()+UserPodcastLike.objects.filter(user=request.user).count()
        saved = UserMusicList.objects.filter(user=request.user).count()+UserVideoList.objects.filter(user=request.user).count()+UserPodcastList.objects.filter(user=request.user).count()
        musicitems = list(MusicPack.objects.all())
        music = random.sample(musicitems, 3)
        tvitems = list(VideoPack.objects.all())
        tv = random.sample(tvitems, 3)
        podcastitems = list(PodcastPack.objects.all())
        podcast = random.sample(podcastitems, 3)
        return render(request, 'dashboard.html',{'liked':liked,'saved':saved,'music':music,'tv':tv,'podcast':podcast})
    except UserMusicLike.DoesNotExist or UserVideoLike.DoesNotExist or UserPodcastLike.DoesNotExist or UserMusicList.DoesNotExist or UserVideoList.DoesNotExist or UserPodcastList.DoesNotExist:
        musicitems = list(MusicPack.objects.all())
        music = random.sample(musicitems, 3)
        tvitems = list(VideoPack.objects.all())
        tv = random.sample(tvitems, 3)
        podcastitems = list(PodcastPack.objects.all())
        podcast = random.sample(podcastitems, 3)
        return render(request, 'dashboard.html',
                      { 'music': music, 'tv': tv, 'podcast': podcast})

def creatordashboard(request):
    totalusers = Bio.objects.filter(role='user').count()
    topliked = Bio.objects.all().order_by('-total_likes')
    fivetopliked = Bio.objects.all().order_by('-total_likes')[:5]
    likedranking = 1
    for index,i in enumerate(topliked):
        if i == Bio.objects.get(email=request.user):
            likedranking = index + 1
    topsaved = Bio.objects.all().order_by('-total_saved')
    fivetopsaved = Bio.objects.all().order_by('-total_saved')[:5]
    savedranking = 1
    for index, i in enumerate(topsaved):
        if i == Bio.objects.get(email=request.user):
            savedranking = index + 1
    return render(request, 'creator-dashboard.html',{'totalusers':totalusers,'fivetopliked':fivetopliked,'likedranking':likedranking,'fivetopsaved':fivetopsaved,'savedranking':savedranking})
    # video = VideoPack.objects.filter(uploaded_by=request.user)
    # liked = []
    # saved = []
    # for v in video:
    #     vi = UserVideoLike.objects.filter(show=v)
    #     src = UserVideoList.objects.filter(show=v)
    #     liked+=vi
    #     saved+=src
    # music = MusicPack.objects.filter(uploaded_by=request.user)
    # for m in music:
    #     mu = UserMusicLike.objects.filter(music=m)
    #     src = UserMusicList.objects.filter(music=m)
    #     saved += src
    #     liked+=mu
    # podcasts = PodcastPack.objects.filter(uploaded_by=request.user)
    # for p in podcasts:
    #     po = UserPodcastLike.objects.filter(podcast=p)
    #     src = UserPodcastList.objects.filter(podcast=p)
    #     saved += src
    #     liked+=po
    # users = User.objects.all()
    # toptvliked = User.objects.get(id=2)
    # tvliked=[]
    # sum=[]
    # for user in users:
    #     tvliked += VideoPack.objects.filter(uploaded_by=user)
    #     for i in tvliked:
    #         sum[user] += i.likes

    # return render(request, 'creator-dashboard.html',{'liked':len(liked),'saved':len(saved),'totalusers':totalusers})

def creatorprofile(request,id):
    creator = User.objects.get(id=id)
    podcasts = PodcastPack.objects.filter(uploaded_by=creator)
    videos = VideoPack.objects.filter(uploaded_by=creator)
    music = MusicPack.objects.filter(uploaded_by=creator)
    total = podcasts.count()+videos.count()+music.count()
    topliked = Bio.objects.all().order_by('-total_likes')
    likedranking = 1
    for index, i in enumerate(topliked):
        if i == Bio.objects.get(email=request.user):
            likedranking = index + 1
    topsaved = Bio.objects.all().order_by('-total_saved')
    savedranking = 1
    for index, i in enumerate(topsaved):
        if i == Bio.objects.get(email=creator):
            savedranking = index + 1
    return render(request, 'creator-profile.html',{'creator':creator,'videos':videos,'music':music, 'podcasts':podcasts, 'total':total,'likedranking':likedranking,'savedranking':savedranking})

def resetimage(request):
    if request.method == 'POST' and request.FILES['image']:
        img = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
        user = request.user
        Bio.objects.filter(email=user).update(image=file)
        return redirect('accountsettings')
    else:
        bio=Bio.objects.get(email=request.user)
        bio.image.delete()
        bio.save()
        return redirect('accountsettings')

def editprofile(request):
    if request.method == 'POST':
        email = request.POST['email']
        image = request.FILES['image']
        fs = FileSystemStorage()
        doc = fs.save(image.name, image)
        user = request.user
        user.set_password(request.POST['password'])
        user.email = email
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.save()
        Bio.objects.get(email=user).update(name =request.POST['email'],image=doc)
        return redirect('dashboard')
    else:
        return render(request, 'account-settings.html')

def deleteaccount(request):
    user = request.user
    user.delete()
    return redirect('home')

def uploadcontent(request):
    packs = []
    tvpacks = VideoPack.objects.filter(uploaded_by=request.user)
    musicpacks = MusicPack.objects.filter(uploaded_by=request.user)
    podcastpacks = PodcastPack.objects.filter(uploaded_by=request.user)
    packs+=tvpacks
    packs+=musicpacks
    packs+=podcastpacks
    return render(request,'upload-content.html',{'packs':packs})

def uploadtvpack(request):
    image = request.FILES['image']
    fs = FileSystemStorage()
    doc = fs.save(image.name, image)
    tvpack = VideoPack(name=request.POST['name'],uploaded_by=request.user,genre=request.POST['genre'],type=request.POST['type'],description=request.POST['description'],uploaded_date=datetime.now(),image=doc)
    tvpack.save()
    return redirect('uploadcontent')

def uploadmusicpack(request):
    image = request.FILES['image']
    fs = FileSystemStorage()
    doc = fs.save(image.name, image)
    musicpack = MusicPack(name=request.POST['name'],uploaded_by=request.user,genre=request.POST['genre'],type=request.POST['type'],description=request.POST['description'],uploaded_date=datetime.now(),image=doc)
    musicpack.save()
    return redirect('uploadcontent')

def uploadpodcastpack(request):
    image = request.FILES['image']
    fs = FileSystemStorage()
    doc = fs.save(image.name, image)
    podcastpack = PodcastPack(name=request.POST['name'],uploaded_by=request.user,genre=request.POST['genre'],description=request.POST['description'],uploaded_date=datetime.now(),image=doc)
    podcastpack.save()
    return redirect('uploadcontent')

def uploadsrc(request):
    src = request.FILES['src']
    fs = FileSystemStorage()
    doc = fs.save(src.name, src)
    id = request.POST['id']
    name = request.POST['pack']
    try:
        tvpack = VideoPack.objects.get(id=id, name = name, uploaded_by=request.user)
        repo = VideoRepo(document_name=request.POST['srcname'],document_src=doc,videopack=tvpack)
        repo.save()
        return redirect('uploadcontent')
    except VideoPack.DoesNotExist:
        try:
            musicpack = MusicPack.objects.get(id=id, name = name, uploaded_by=request.user)
            repo = MusicRepo(document_name=request.POST['srcname'], document_src=doc, musicpack=musicpack)
            repo.save()
            return redirect('uploadcontent')
        except MusicPack.DoesNotExist:
            podcastpack = PodcastPack.objects.get(id=id, name = name, uploaded_by=request.user)
            repo = PodcastRepo(document_name=request.POST['srcname'], document_src=doc, podcastpack=podcastpack)
            repo.save()
            return redirect('uploadcontent')

def creatorinfo(request,id):
    creator = User.objects.get(id=id)
    podcasts = PodcastPack.objects.filter(uploaded_by=creator)
    videos = VideoPack.objects.filter(uploaded_by=creator)
    music = MusicPack.objects.filter(uploaded_by=creator)
    return render('creator-info.html', {'creator':creator,'videos':videos,'music':music, 'podcasts':podcasts})

#Create new bio API
class BioList(generics.ListCreateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    def perform_create(self, serializer):
        try:
            user = User.objects.get(username=self.request.data['user'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#Update User Bio API
class Bioupdate(generics.RetrieveUpdateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    def perform_create(self, serializer):
        try:
            user = User.objects.get(username=self.request.data['user'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)