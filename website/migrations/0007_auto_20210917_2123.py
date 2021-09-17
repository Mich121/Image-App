# Generated by Django 3.1.7 on 2021-09-17 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210917_2031'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thumbnails',
            new_name='Thumbnail_200',
        ),
        migrations.CreateModel(
            name='Thumbnail_Original',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.images')),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail_400',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.images')),
            ],
        ),
    ]