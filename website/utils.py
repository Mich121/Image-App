from .models import Thumbnail_Basic, Thumbnail_Premium, Thumbnail_Enterprise
from PIL import Image

def Make_Thumbnail(path, height, width, name, instance):
        image = Image.open(path)
        image.thumbnail((height,width))
        #create thumbnail in our disc 
        image.save(f"media/thumbnails/thumbnail_{height}x{width}_" + name)
        #create object (link to thumbnail) in database
        if height == 200:
            Thumbnail_Basic.objects.create(image_id=instance, owner=instance.owner, thumb_basic=f"thumbnails/thumbnail_{height}x{width}_" + name)
        elif height == 400:
            Thumbnail_Premium.objects.create(image_id=instance, owner=instance.owner, thumb_premium=f"thumbnails/thumbnail_{height}x{width}_" + name)
        else:
            Thumbnail_Enterprise.objects.create(image_id=instance, owner=instance.owner, thumb_enterprise = f"thumbnails/thumbnail_{height}x{width}_" + name)