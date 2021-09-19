from .models import Thumbnail_200, Thumbnail_400
from PIL import Image

def Make_Thumbnail(path, height, width, name, instance):
        image = Image.open(path)
        image.thumbnail((height,width))
        #create thumbnail in our disc 
        image.save(f"media/thumbnails/thumbnail_{height}x{width}_" + name)
        #create object (link to thumbnail) in database
        if height == 200:
            Thumbnail_200.objects.create(image_id=instance, owner=instance.owner, thumb_200=f"thumbnails/thumbnail_{height}x{width}_" + name)
        elif height == 400:
            Thumbnail_400.objects.create(image_id=instance, owner=instance.owner, thumb_400=f"thumbnails/thumbnail_{height}x{width}_" + name)