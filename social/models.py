from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    video = models.FileField(upload_to='uploads/post_videos/', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE )

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

