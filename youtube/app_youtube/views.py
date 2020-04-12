from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Videos, Comments, Likes, Dislikes, UserViews
from .forms import VideoSearchForm,  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    videos = Videos.objects.all()
    return render(request, 'index.html', {'videos': videos})

# @login_required(login_url='app_youtube:login')
def video_open(request, video_id):
    open_video = get_object_or_404(Videos, pk=video_id)
    user = get_object_or_404(Users, pk=1)
    videos = Videos.objects.all()
    view_videos = UserViews.objects.all()
    
    if request.method == 'POST':
        cm = Comments.objects.create(
            video = open_video,
            username = user,
            describe = request.POST.get('commenttt'),
            post_date = '2020-04-10'
        )
        cm.save()
    
    return render(request, 'video_open.html', {
        'open_video':open_video,
        'videos': videos,
        'view_videos': view_videos,
        # 'videos': videos,
        'post_active': True
    })
    
def video_like_dislike(request, videos_id):
    videos = get_object_or_404(Videos, pk=videos_id)
    like = videos.like_video
    dislike = videos.dislike_video
    Videos.objects.filter(pk=videos_id).update(like_video = like+1)
    Videos.objects.filter(pk=videos_id).update(dislike_video = dislike+1)
    return redirect('video/'+str(videos_id)+'/')

# search video
def videos(request):
    searchvalue=''
    form= VideoSearchForm(request.POST or None)
    if form.is_valid():
        searchvalue= form.cleaned_data.get("search")

    searchresults= Videos.objects.filter(title__icontains= searchvalue)
    context= {'form': form,
              'searchresults': searchresults,
              }
    
    return render(request, 'searchpage.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('app_youtube:index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'account was created for' + user)
                return redirect('app_youtube:login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('app_youtube:index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password= password)
            
            if user is not None:
                login(request, user)
                return redirect('app_youtube:index')
            else:
                messages.info(request, 'username or password is incorrect')
        
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('app_youtube:login')

