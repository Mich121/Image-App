from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload_image/', views.AddImage.as_view(), name='upload_image'),
    path('my_images/', views.MyImages.as_view(), name='my_images'),
]
