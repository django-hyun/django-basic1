from django.db import models
from django.db.models.fields.related import ForeignKey
from django.conf import settings


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo=models.ImageField(blank=True, upload_to='instagram/post/%Y%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='instagram_post_set')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Tag(models.Model):
   name = models.CharField(max_length=50, unique=True)
   
   def __str__(self):
      return self.name