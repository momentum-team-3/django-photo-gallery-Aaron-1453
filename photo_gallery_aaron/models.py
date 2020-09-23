from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

from users.models import User

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='photo', null=True)
    image_medium = ImageSpecField(source='photo',
                                            processors=[ResizeToFit(300, 300)], format='jpeg', options={'quality': 80})
    image_thumbnail = ImageSpecField(source='photo',
                                            processors=[ResizeToFill(300, 300)], format='jpeg', options={'quality': 80})                                        
                                            
    gallery = models.ForeignKey(to='Gallery', null=True, on_delete=models.CASCADE, related_name='gallery_photos')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner_photos', null=True, blank=True)
    pinned = models.BooleanField(default=False)
    
    
class Comment(models.Model):
    text = models.TextField(max_length=600)
    pub_date = models.DateTimeField
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name='comments')
    
    
class Gallery(models.Model):
    # default_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name='+')
    photos = models.ManyToManyField(to=Photo, related_name='galleries', blank=True)
    title = models.CharField(max_length=600)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="galleries", blank=True)