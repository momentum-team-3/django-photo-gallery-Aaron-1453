from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    # profile_photo = models.ImageField
    pass

# class Gallery(models.Model):
#     default_photo = models.ForeignKey(to=Photo)
#     title = models.CharField(max_length=600)
#     public = models.BooleanField(default=False)
#     owner = models.ForeignKey(to=User)
    

# class Photo(models.Model):
#     image = models.ImageField
#     gallery = models.ForeignKey(to=Gallery)
#     owner = models.ForeignKey(to=User)
#     pinned = models.BooleanField(default=False)
    

# class Comment(models.Model):
#     text = models.TextField(max_length=600)
#     date = models.DateTimeField
#     author = models.ForeignKey(to=User)
#     photo = models.ForeignKey(to=Photo)
   