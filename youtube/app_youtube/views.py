from django.shortcuts import render, get_object_or_404
from .models import Users, Videos, Comments, Likes, Dislikes, UserViews
from .forms import VideoSearchForm

# Create your views here.
def index(request):
    videos = Videos.objects.all()
    return render(request, 'index.html', {'videos': videos})

def video_open(request, video_id):
    open_video = get_object_or_404(Videos, pk=video_id)
    videos = Videos.objects.all()
    comments = Comments.objects.all()
    view_videos = UserViews.objects.all()
    return render(request, 'video_open.html', {
        'open_video':open_video,
        'videos': videos,
        'comments': comments,
        'view_videos': view_videos
    })
    
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