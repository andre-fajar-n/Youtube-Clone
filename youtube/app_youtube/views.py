from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Videos, Comments, Likes, Dislikes, UserViews
from .forms import VideoSearchForm,  CreateUserForm, CommentForm
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
    videos = Videos.objects.all()
    view_videos = UserViews.objects.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_youtube:video_open')
    else:
        form = CommentForm()
    
    return render(request, 'video_open.html', {
        'open_video':open_video,
        'videos': videos,
        'view_videos': view_videos,
        'form': form
    })

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

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})