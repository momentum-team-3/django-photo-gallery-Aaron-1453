from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Comment, Gallery
from .forms import GalleryForm, PhotoForm, CommentForm

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
    """Returns list of galleries for gallery view."""
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    photos = gallery.photos.all()
    return render(request, "gallery/view_gallery.html", {
        'gallery': gallery,
        'photos': photos,
        "gallery_pk": gallery_pk,
    })
    
def user_galleries(request):
    """list of all galleries belonging to user"""
    galleries = request.user.galleries.all()
    return render(request, "gallery/user_galleries.html", {
        'galleries': galleries,
    })
    
def edit_gallery(request, gallery_pk):
    gallery = get_object_or_404(request.user.galleries, pk=gallery_pk)
    if request.method == "GET":
        form = GalleryForm(instance=gallery)
    else:
        form = GalleryForm(instance=gallery, data=request.POST)
        if form.is_valid():
            gallery = form.save()
            return redirect(to="view_gallery", pk=gallery_pk)        
    return render(request, 'gallery/edit_gallery.html', 
        {"form": form, "gallery": gallery,}) 
        
def view_photo(request, photo_pk):
    """Return list of details for a photo."""
    photo = get_object_or_404(request.user.owner_photos, pk=photo_pk)
    return render(request, "photo/view_photo.html", {
        'photo': photo,
        'photo_pk': photo_pk,
    })

def user_photos_list(request):
    photos = request.user.owner_photos.all()
    return render(request, "photo/user_photos_list.html", {
        "photos": photos
    })

def upload_photo(request):
    if request.method == "GET":
        form = PhotoForm()
    else:
        form = PhotoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.save()
            return redirect(to='user_photos_list')
    return render(request, "photo/upload_photo.html", {
        'form':form
        })

def delete_photo(request, photo_pk):
    """Delete photo from user account."""
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.method == "POST":
        photo.delete()
        return redirect('user_photos_list')
    return render (request, 'photo/delete_photo.html', {
        'photo': photo
    })

def photo_comment(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.method == "GET":
        form = CommentForm()
    else:   
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.photo = photo
            comment.save()
            return redirect(to='view_photo', photo_pk=photo_pk)
    return render(request, 'photo/photo_comment.html',
                      {'form': form, 'photo': photo})
# # goes to url, comment on photo, and takes them back to photo

def delete_gallery(request, gallery_pk):
    """Delete gallery from user account."""
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    if request.method == "POST":
        gallery.delete()
        return redirect('user_galleries')
    return render (request, 'gallery/delete_gallery.html', {
        'gallery': gallery
    })

# def delete_gallery(request, gallery_id):
#     return HttpResponse("Youre looking at '{% gallery.title %}'")

def logout(request):
    return render(request, 'logout.html')

# def view_profile(request):
#     """Return user details, uploaded photos and galleries."""
#     return HttpResponse('view_profile')