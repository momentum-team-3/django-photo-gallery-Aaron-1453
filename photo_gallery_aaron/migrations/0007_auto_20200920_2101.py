# Generated by Django 3.1.1 on 2020-09-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery_aaron', '0006_auto_20200920_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/'),
        ),
    ]