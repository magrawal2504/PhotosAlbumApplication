from rest_framework import serializers
from album_photoapp.models import Album, Photo
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image_url',  'owner', 'album']


class PhotoSerializerNesting(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['image_url', 'owner']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializerNesting(many=True, read_only=True, source='photo_set')

    class Meta:
        model = Album
        fields = ['name', 'photos']
