# Generated by Django 3.1.1 on 2020-09-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery_aaron', '0003_auto_20200918_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='default_photo',
        ),
    ]
