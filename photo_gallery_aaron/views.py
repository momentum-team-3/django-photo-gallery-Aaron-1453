from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Comment, Gallery
from .forms import GalleryForm

from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "homepage.html", {}) 

def add_gallery(request):
    if request.method == "GET":
        form = GalleryForm()
    else:
        form = GalleryForm(data=request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.owner = request.user
            gallery.save()
            return redirect(to='view_gallery', gallery_pk=gallery.pk)
    return render(request, "gallery/add_gallery.html", {'form':form})

def view_gallery(request, gallery_pk):
    """Returns list of photos for gallery view."""
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    photos = gallery.photos.all()
    return render(request, "gallery/view_gallery.html", {
        'gallery': gallery,
        'photos': photos,
        "gallery_pk": gallery_pk
    })
    
def user_galleries(request):
    """list of all galleries belonging to user"""
    galleries = request.user.gallery_owner(all)
    return render(request, "gallery/user_galleries.html", {
        'galleries': galleries,
    })
    
    
def edit_gallery(request):
    return HttpResponse('edit_gallery')

def photo_detail(request):
    """Return list of details for a photo."""
    return HttpResponse('photo_detail')

def upload_photo(request):
    """Give user ability to save photos to gallery."""
    return HttpResponse('upload_photo')

def delete_photo(request):
    """Delete photo from user account."""
    return HttpResponse('delete_photo')

def photo_comment(request):
    """Add comment to a photo."""
# # goes to url, comment on photo, and takes them back to photo
    return HttpResponse('photo_comment')

# def view_profile(request):
#     """Return user details, uploaded photos and galleries."""
#     return HttpResponse('view_profile')