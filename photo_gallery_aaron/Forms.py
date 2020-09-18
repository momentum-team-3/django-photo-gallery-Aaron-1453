from django import forms
from .models import Photo, Gallery, Comments

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'title',
            'public'
        ]