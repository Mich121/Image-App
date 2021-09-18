from rest_framework import serializers
from .models import Images, Thumbnail_Basic, Thumbnail_Enterprise, Thumbnail_Premium

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title', 'file')
        
class Thumbnail_Basic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_Basic
        fields = '__all__'
        
class Thumbnail_Premium_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_Premium
        fields = '__all__'
        
class Thumbnail_Enterprise_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_Enterprise
        fields = '__all__'