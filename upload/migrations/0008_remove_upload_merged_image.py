# Generated by Django 3.1.4 on 2020-12-16 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_upload_merged_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='merged_image',
        ),
    ]
