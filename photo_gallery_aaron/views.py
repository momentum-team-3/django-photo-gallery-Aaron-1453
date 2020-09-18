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
            form.save()
            return redirect(to='view_gallery')

def view_gallery(request):
    """Returns list of photos for gallery view."""
    # photos = Photo.objects.all()
    # return render(request, "photos/detail")
    # include logic to order photo list by pinned photos
    
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