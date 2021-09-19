from django.db import models
from profiles.models import CustomUser
from django.urls import reverse

# Create your models here.
class Images(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title + ' | ' + str(self.owner)

class Thumbnail_200(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_200 = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return str(self.image_id.title) + '_thumbnail_200_' + ' | '  + str(self.image_id.owner)
        
class Thumbnail_400(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_400 = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return str(self.image_id.title) + '_thumbnail_400_' + ' | '  + str(self.image_id.owner)

class Thumbnail_Configurable(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumb_configurable = models.ImageField(upload_to='thumbnails/')
    thumb_width = models.PositiveIntegerField(default=0)
    thumb_height = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.thumb_configurable) + '_thumbnail_configurable_'

    def get_absolute_url(self):
        return reverse('home')