from .models import Thumbnail_Basic, Thumbnail_Premium, Thumbnail_Enterprise
from PIL import Image

def Make_Thumbnail(path, height, width, name, instance):
        image = Image.open(path)
        image.thumbnail((height,width)) 
        image.save(f"media/thumbnails/thumbnail_{height}x{width}_" + name)
        if height == 200:
            obj = Thumbnail_Basic.objects.create(image_id=instance, owner=instance.owner)
            obj.thumb_basic = f"thumbnails/thumbnail_{height}x{width}_" + name
            obj.save()
        elif height == 400:
            obj = Thumbnail_Premium.objects.create(image_id=instance, owner=instance.owner)
            obj.thumb_premium = f"thumbnails/thumbnail_{height}x{width}_" + name
            obj.save()
        else:
            obj = Thumbnail_Enterprise.objects.create(image_id=instance, owner=instance.owner)
            obj.thumb_enterprise = f"thumbnails/thumbnail_{height}x{width}_" + name
            obj.save() 