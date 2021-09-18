from PIL.Image import blend
from django.db import models
from profiles.models import CustomUser
from django.urls import reverse

# Create your models here.
class Images(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to="images/", width_field='image_width', height_field='image_height')

    def __str__(self):
        return self.title + ' | ' + str(self.owner)

class Thumbnail_Basic(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_basic = models.ImageField(upload_to='thumbnails/', blank=True),

    def __str__(self):
        return str(self.image_id.title) + '_thumbnail_basic_' + ' | '  + str(self.image_id.owner)
        
class Thumbnail_Premium(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_premium = models.ImageField(upload_to='thumbnails/', blank=True),

    def __str__(self):
        return str(self.image_id.title) + '_thumbnail_premium_' + ' | '  + str(self.image_id.owner)
        
class Thumbnail_Enterprise(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_enterprise = models.ImageField(upload_to='thumbnails/', blank=True),

    def __str__(self):
        return str(self.image_id.title) + '_thumbnail_enterprise_' + ' | ' + str(self.image_id.owner)