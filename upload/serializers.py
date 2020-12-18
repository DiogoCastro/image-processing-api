from rest_framework import serializers

from .models import Upload


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = [
            'url',
            'id',
            'main_image',
            'water_mark',
        ]
