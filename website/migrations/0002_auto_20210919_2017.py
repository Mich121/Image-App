# Generated by Django 3.1.7 on 2021-09-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='images',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]