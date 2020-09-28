from django import forms
from .models import Photo, Gallery, Comment

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'title',
            'public'
        ]
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'photo'
        ]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

