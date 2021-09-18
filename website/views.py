from django.views import generic
from website.serializers import ImageSerializer, Thumbnail_Basic_Serializer, Thumbnail_Premium_Serializer, Thumbnail_Enterprise_Serializer
from .models import Images, Thumbnail_Basic, Thumbnail_Premium, Thumbnail_Enterprise
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

class MyThumbnails_Basic(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_Basic_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_Basic.objects.filter(owner=self.request.user)
        
class MyThumbnails_Premium(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_Premium_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_Premium.objects.filter(owner=self.request.user) 

class MyThumbnails_Enterprise(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Thumbnail_Enterprise_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_Enterprise.objects.filter(owner=self.request.user)