from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload_image/', views.AddImage.as_view(), name='upload_image'),
    path('my_images_link/', views.MyImagesLink.as_view(), name='my_images_link'),
    path('my_images/', views.MyImages.as_view(), name='my_images'),
    path('my_thumbnails_200/', views.MyThumbnails_200.as_view(), name='my_thumbnails_200'),
    path('my_thumbnails_400/', views.MyThumbnails_400.as_view(), name='my_thumbnails_400'),
]
