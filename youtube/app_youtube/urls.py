from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'app_youtube'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:video_id>/', views.video_open, name='video_open'),
    # path('video/like_video/<int:video_id>/', views.video_like_dislike),
    # path('video/dislike_video/<int:video_id>/', views.video_like_dislike),
    path('search/', views.video_search, name='search'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)