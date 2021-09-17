from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Images, Thumbnail_200, Thumbnail_400, Thumbnail_Original
from PIL import Image
from rest_framework import status
from rest_framework.response import Response
from urllib.request import urlopen

@receiver(post_save, sender = Images)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        try:
            path = 'media/' + str(instance.file)
            name = str(instance.file).replace('images/', '')
            with Image.open(path) as image:
                if instance.owner.basic: 
                    image.thumbnail((200,200))
                    image.save('media/thumbnails/thumbnail_200_' + name)
                    obj = Thumbnail_200.objects.create(image=instance.id, thumb_200='media/thumbnails/thumbnail_200_' + name)
                    print(obj)
                elif instance.owner.premium:
                    image_200 = image.thumbnail((200,200)) 
                    image_400 = image.thumbnail((400,400)) 
                    #Thumbnails.objects.create(image=instance.id, thumb_200=image_200, thumb_400=image_400, thumb_original='')     
                elif instance.owner.enterprise:
                    image_200 = image.thumbnail((200,200)) 
                    image_400 = image.thumbnail((400,400))
                    image_original = image.thumbnail((instance.height,instance.width)) 
                    #Thumbnails.objects.create(image=instance.id, thumb_200=image_200, thumb_400=image_400, thumb_original=image_original)
        except:
            return Response({'Error':'Thumbnails have not been created!'}, status=status.HTTP_417_EXPECTATION_FAILED)