from django.views import generic
from website.serializers import ImageSerializer
from .models import Images
from django.shortcuts import render
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

