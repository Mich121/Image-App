from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Images
from rest_framework import status
from rest_framework.response import Response
from .utils import Make_Thumbnail

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
                Make_Thumbnail(path, instance.image_height, instance.image_width, name, instance)
            elif instance.owner.enterprise:
                Make_Thumbnail(path, 200, 200, name, instance)
                Make_Thumbnail(path, 400, 400, name, instance)
                Make_Thumbnail(path, instance.image_height, instance.image_width, name, instance)
        except:
            return Response({'Error':'Thumbnails have not been created!'}, status=status.HTTP_417_EXPECTATION_FAILED)
