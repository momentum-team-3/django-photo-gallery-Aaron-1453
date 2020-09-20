# Generated by Django 3.1.1 on 2020-09-19 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_gallery_aaron', '0004_remove_gallery_default_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]