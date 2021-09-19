from rest_framework import serializers
from .models import Images, Thumbnail_200, Thumbnail_400, Thumbnail_Original

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title', 'file')
        
class Thumbnail_200_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_200
        fields = '__all__'
        
class Thumbnail_400_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_400
        fields = '__all__'
        
class Thumbnail_Original_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail_Original
        fields = '__all__'