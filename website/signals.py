from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from .models import Images, Thumbnail_Configurable
from rest_framework import status
from rest_framework.response import Response
from .utils import Make_Thumbnail
from PIL import Image

@receiver(post_save, sender = Images)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        try:
            path = 'media/' + str(instance.file)
            name = str(instance.file).replace('images/', '')
            if instance.owner.basic: 
                Make_Thumbnail(path, 200, 200, name, instance)
            elif instance.owner.premium:
                Make_Thumbnail(path, 200, 200, name, instance)
                Make_Thumbnail(path, 400, 400, name, instance)
            elif instance.owner.enterprise:
                Make_Thumbnail(path, 200, 200, name, instance)
                Make_Thumbnail(path, 400, 400, name, instance)
        except:
            return Response({'Error':'Thumbnails have not been created!'}, status=status.HTTP_417_EXPECTATION_FAILED)

@receiver(pre_save, sender = Thumbnail_Configurable)
def create_config_thumb(sender, instance, **kwargs):
    try:
        path = 'media/' + str(instance.thumb_configurable)
        name = str(instance.thumb_configurable).replace('images/', '')
        image = Image.open(path)
        image.thumbnail((instance.thumb_width, instance.thumb_height))
        image.save(f"{path}X{instance.thumb_width}x{instance.thumb_height}_")
        instance.thumb_configurable = f"media/thumbnails/thumbnail__configurable_{instance.thumb_width}x{instance.thumb_height}_"
        instance.save()
    except:
        return Response({'Error':'Thumbnails have not been created!'}, status=status.HTTP_417_EXPECTATION_FAILED)