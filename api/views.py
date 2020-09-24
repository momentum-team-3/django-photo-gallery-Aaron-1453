from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import Response, APIView
from photo_gallery_aaron.models import Gallery
from api.serializers import GallerySerializer
from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404

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
        serializer.save(owner=self.request.user)
        
class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    
    def get_queryset(self):
        return self.request.user.galleries

# class GalleryViewSet(viewset.ModelViewSet):
#     serializer_class = GallerySerializer
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
        
#     def get_queryset(self):
#         if self.action in ['list', 'create', 'retrieve']:
#             return self.request.user.galleries
        
# class PhotoImageView(APIView):
#     def put(self, request, pk):
#         get_object_or_404(self.request.user.photos, pk=pk)
#         #read the uploaded file
#         #set image on the recipe to the uploaded file
#         #save the recipe
#         #let the user know things are good
#         if 'file' not in request.data:
#             raise ParseError('empty content')
        
#         file=request.data['file']
#         photo.image.save(file.name, file, save=True)
#         return Response(status=status.HTTP_200_OK)