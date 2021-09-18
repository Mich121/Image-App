from django.contrib import admin
from .models import Images, Thumbnail_Enterprise, Thumbnail_Basic, Thumbnail_Premium

# Register your models here.
admin.site.register(Images)
admin.site.register(Thumbnail_Basic)
admin.site.register(Thumbnail_Premium)
admin.site.register(Thumbnail_Enterprise)