# Generated by Django 3.2.25 on 2025-01-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20250112_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/post_videos/'),
        ),
    ]