from django.contrib import admin
from .models import Images, Thumbnail_Original, Thumbnail_200, Thumbnail_400

# Register your models here.
admin.site.register(Images)
admin.site.register(Thumbnail_200)
admin.site.register(Thumbnail_400)
admin.site.register(Thumbnail_Original)