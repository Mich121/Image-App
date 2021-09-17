from django.db import models
from django.utils.translation import gettext_lazy
from profiles.models import CustomUser
from django.urls import reverse

# Create your models here.
class Images(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.ImageField(gettext_lazy("Image"), upload_to="images/")

    def __str__(self):
        return self.title + ' | ' + str(self.owner)