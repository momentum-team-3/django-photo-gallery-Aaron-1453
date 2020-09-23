from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import Response, APIView
from photo_gallery_aaron.models import Gallery
from api.serializers import GallerySerializer
from rest_framework import generics

# @api_view(http_method_names=['GET'])
# def gallery_list(request):
#     galleries = Gallery.objects.for_user(request.user)
#     serializer = GallerySerializer(galleries, many=True)
#     return Response(serializer.data)

class GalleryListView(generics.ListCreateAPIView):
    serializer_class = GallerySerializer
    
    def get_queryset(self):
        return self.request.user.galleries
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.owner)