from django.views import generic
from website.serializers import ImageSerializer, Thumbnail_200_Serializer, Thumbnail_400_Serializer, Thumbnail_Configurable_Serializer
from .models import Images, Thumbnail_200, Thumbnail_400, Thumbnail_Configurable
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ConfigurableThumbForm

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

class MyImages(LoginRequiredMixin, generic.ListView):
    model = Images
    template_name = 'my_images.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        images = Images.objects.filter(owner=user.id)
        context['images'] = images
        return context

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class MyImagesLink(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated&ReadOnly]
    serializer_class = ImageSerializer
    login_url = 'login'

    def get_queryset(self):
        return Images.objects.filter(owner=self.request.user)

class MyThumbnails_200(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated&ReadOnly]
    serializer_class = Thumbnail_200_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_200.objects.filter(owner=self.request.user)
        
class MyThumbnails_400(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated&ReadOnly]
    serializer_class = Thumbnail_400_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_400.objects.filter(owner=self.request.user) 

class CreateConfigurableThumbnails(LoginRequiredMixin, generic.CreateView):
    model = Thumbnail_Configurable
    form_class = ConfigurableThumbForm
    template_name = 'create_config_thumb.html'
    login_url = 'login'
    
class MyConfigurableThumbnails(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser, ReadOnly]
    serializer_class = Thumbnail_Configurable_Serializer
    login_url = 'login'

    def get_queryset(self):
        return Thumbnail_Configurable.objects.filter(owner=self.request.user)