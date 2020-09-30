from rest_framework import serializers
from photo_gallery_aaron.models import Gallery, Photo

class GallerySerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Gallery
        fields = [
            'photos',
            'title',
            'public',
            'owner', 
        ]
        
class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Photo
        fields = [
            'photo',
            'gallery',
            'owner',
        ]
    