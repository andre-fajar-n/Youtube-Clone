from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    birthday = models.DateField(auto_now=True, blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(
        max_length=1,
        choices = gender_choices,
        default = 'M'
    )
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class Videos(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    list_category = [
        ('FA', 'Film & Animation'),
        ('AV','Autos & Vehicles'),
        ('M','Music'),
        ('PA','Pets & Animals'),
        ('S','Sports'),
        ('TE','Travel & Events'),
        ('G','Gaming'),
        ('PB','People & Blogs'),
        ('C','Comedy'),
        ('En','Entertainment'),
        ('NP','News & Politics'),
        ('HS','Howto & Style'),
        ('Ed','Education'),
        ('ST','Science & Technology'),
        ('NA','Nonprofits & Activism')
    ]
    category = models.CharField(max_length=2, choices=list_category, default='FA')
    post_date = models.DateTimeField( auto_now=True, blank=True)
    keywords = models.CharField(max_length=255, default='')
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    describe = models.TextField()
    post_date = models.DateTimeField(blank=True, auto_now=True)
    
    class Meta:
        ordering = ['post_date']
    
    def __str__(self):
        return 'Comment %s by %s'%(self.describe, self.username)
    
class Likes(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.username) + ' like'
    
class Dislikes(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username + ' dislike'
    
class UserViews(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username + ' view'