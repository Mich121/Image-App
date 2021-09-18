from rest_framework import serializers
from .models import Images, Thumbnail_Basic, Thumbnail_Enterprise, Thumbnail_Premium
import json
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('owner', 'title', 'file')
        
class Thumbnail_Basic_Serializer(serializers.ModelSerializer):
    thumb_url = serializers.SerializerMethodField('get_thumb_url')
    class Meta:
        model = Thumbnail_Basic
        fields = ('image_id', 'owner', 'thumb_url')

    def get_thumb_url(self, obj):
        return json.dumps(str(obj.thumb_basic))
        
class Thumbnail_Premium_Serializer(serializers.ModelSerializer):
    thumb_url = serializers.SerializerMethodField('get_thumb_url')
    class Meta:
        model = Thumbnail_Premium
        fields = ('image_id', 'owner', 'thumb_url')

    def get_thumb_url(self, obj):
        return json.dumps(str(obj.thumb_premium))
        
class Thumbnail_Enterprise_Serializer(serializers.ModelSerializer):
    thumb_url = serializers.SerializerMethodField('get_thumb_url')
    class Meta:
        model = Thumbnail_Enterprise
        fields = ('image_id', 'owner', 'thumb_url')

    def get_thumb_url(self, obj):
        return json.dumps(str(obj.thumb_enterprise))