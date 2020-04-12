from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    birthday = models.DateField(default=datetime.now(), blank=True)
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
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=255, default='')
    post_date = models.DateTimeField(default=datetime.now(), blank=True)
    keywords = models.CharField(max_length=255, default='')
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    describe = models.TextField()
    post_date = models.DateTimeField(default=datetime.now(), blank=True)
    
    def __str__(self):
        return self.username + ' comment'
    
class Likes(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username + ' like'
    
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