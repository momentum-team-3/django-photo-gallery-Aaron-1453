from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "homepage.html", {}) 

# def create_gallery(request):
#     return HttpResponse("create gallery view")

# def view_gallery(request):
    """Returns list of photos for gallery view."""
    # include logic to order photo list by pinned photos
    
# def edit_gallery(request):
    
# def photo_detail(request):
    """Return list of details for a photo."""

# def upload_photo(request):
    """Give user ability to save photos to gallery."""

# def delete_photo(request):
    """Delete photo from user account."""

# def make_comment(request):
    """Add comment to a photo."""
# # goes to url, comment on photo, and takes them back to photo

# def user_detail_view(request):
    """Return user details, uploaded photos and galleries."""