# Generated by Django 3.1.4 on 2020-12-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='merged_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]