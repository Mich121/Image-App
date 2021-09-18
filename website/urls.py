from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload_image/', views.AddImage.as_view(), name='upload_image'),
    path('my_images/', views.MyImages.as_view(), name='my_images'),
    path('my_thumbnails_basic/', views.MyThumbnails_Basic.as_view(), name='my_thumbnails_basic'),
    path('my_thumbnails_premium/', views.MyThumbnails_Premium.as_view(), name='my_thumbnails_premium'),
    path('my_thumbnails_enterprise/', views.MyThumbnails_Enterprise.as_view(), name='my_thumbnails_enterprise'),
]
