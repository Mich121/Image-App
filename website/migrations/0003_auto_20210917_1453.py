# Generated by Django 3.1.7 on 2021-09-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_images_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='images',
            name='image_width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(height_field='image_height', upload_to='images/', verbose_name='Image', width_field='image_width'),
        ),
    ]