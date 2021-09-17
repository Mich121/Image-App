from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title', 'file')