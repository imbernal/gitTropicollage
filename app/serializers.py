from rest_framework import serializers
from .models import *


class CasaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Casa
        fields = ('nombre', 'municipio', 'precio_alta')


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = ('title', 'images')


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('file',)
