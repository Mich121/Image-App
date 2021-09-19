from django.views import generic
from website.serializers import ImageSerializer, Thumbnail_200_Serializer, Thumbnail_400_Serializer, Thumbnail_Original_Serializer
from .models import Images, Thumbnail_200, Thumbnail_400, Thumbnail_Original
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = 'login'

class AddImage(LoginRequiredMixin, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    login_url = 'login'

    #connect image with user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MyImages(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    login_url = 'login'

    def get_queryset(self):
        return Images.objects.filter(owner=self.request.user)

class MyThumbnails_200(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_200_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_200.objects.filter(owner=self.request.user)
        
class MyThumbnails_400(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_400_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_400.objects.filter(owner=self.request.user) 

class MyThumbnails_Original(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_Original_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_Original.objects.filter(owner=self.request.user)