# Generated by Django 3.1.4 on 2020-12-16 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_remove_upload_merged_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='merged_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='_static'),
            preserve_default=False,
        ),
    ]
