from django.db import models


class Upload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to='_static')
    water_mark = models.ImageField(upload_to='_static')

    class Meta:
        ordering = ['created']
