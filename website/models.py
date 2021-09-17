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

class Thumbnail_200(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    thumb_200 = models.ImageField(),

    def __str__(self):
        return str(self.image_id) + '_200_'
        
class Thumbnail_400(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    thumb_400 = models.ImageField(),

    def __str__(self):
        return str(self.image_id) + '_400_'
        
class Thumbnail_Original(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    thumb_original = models.ImageField(),

    def __str__(self):
        return str(self.image_id) + '_original_'