from django.db import models

from users.models import User

# Create your models here.
class Photo(models.Model):
    image = models.ImageField
    # gallery = models.ForeignKey(to=Gallery, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)
    
    
class Comment(models.Model):
    text = models.TextField(max_length=600)
    pub_date = models.DateTimeField
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    
    
class Gallery(models.Model):
    default_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    title = models.CharField(max_length=600)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
