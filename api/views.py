from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import Response, APIView
from photo_gallery_aaron.models import Gallery
from api.serializers import GallerySerializer, PhotoSerializer
from rest_framework import generics, viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser, ParseError


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


# lines 33 -41 are equivalent to lines 16 through 29, I have not tested them though
# class GalleryViewSet(viewset.ModelViewSet):
#     serializer_class = GallerySerializer
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
        
#     def get_queryset(self):
#         if self.action in ['list', 'create', 'retrieve']:
#             return self.request.user.galleries
        
class PhotoImageView(APIView):
    parser_classes = (FileUploadParser, )
    def put(self, request, pk):
        photo = get_object_or_404(self.request.user.owner_photos, pk=pk)
        #read the uploaded file
        #set image on the uploaded file
        #save the image
        #let the user know things are good
        if 'file' not in request.data:
            raise ParseError('empty content')
        file = request.data['file']
        photo.photo.save(file.name, file, save=True)
        return Response(status=status.HTTP_200_OK)
    
class PhotoListView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    
    def get_queryset(self):
        return self.request.user.owner_photos
    
class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    
    def get_queryset(self):
        return self.request.user.owner_photos