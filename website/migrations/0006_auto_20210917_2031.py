# Generated by Django 3.1.7 on 2021-09-17 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210917_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnails',
            name='thumb_200',
        ),
        migrations.RemoveField(
            model_name='thumbnails',
            name='thumb_400',
        ),
        migrations.RemoveField(
            model_name='thumbnails',
            name='thumb_original',
        ),
    ]