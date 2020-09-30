"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from photo_gallery_aaron import views
from django.conf.urls.static import static
from api import views as api_views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/logout/', views.logout, name='logout'),
# Photo urls
    path('photo/view_photo/<int:photo_pk>/', views.view_photo, name='view_photo'),
    path('photo/gallery_photos_list/', views.gallery_photos_list, name='gallery_photos_list'),
    path('photo/upload_photo/<int:gallery_pk>/', views.upload_photo, name='upload_photo'),
    path('photo/delete_photo/<int:photo_pk>/', views.delete_photo, name='delete_photo'),
    path('photo/photo_comment/<int:photo_pk>/', views.photo_comment, name='photo_comment'),

#Gallery urls
    path('gallery/add_gallery/', views.add_gallery, name='add_gallery'),
    path('gallery/view_gallery/<int:gallery_pk>/', views.view_gallery, name='view_gallery'),
    path('gallery/edit_gallery/<int:gallery_pk>/', views.edit_gallery, name='edit_gallery'),
    path('gallery/user_galleries/', views.user_galleries, name='user_galleries'),
    path('gallery/delete_gallery/<int:gallery_pk>/', views.delete_gallery, name='delete_gallery'),
#Gallery Api urls
    path('api-auth/', include('rest_framework.urls')),
    path('api/galleries/', api_views.GalleryListView.as_view()),
    path('api/galleries/<int:pk>/', api_views.GalleryDetailView.as_view()),
#Photo Api urls
    path('api/photo/<int:pk>/image/', api_views.PhotoImageView.as_view()),
    path('api/photo/', api_views.PhotoListView.as_view()),
    path('api/photo/<int:pk>/', api_views.PhotoDetailView.as_view()),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
