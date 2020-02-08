from rest_framework import serializers
from django.db.models import Q

from .models import SongShi
from .models import SongAuthor

class SongShiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongShi
        # fields = "__all__"
        fields = ['author', 'content', 'strains', 'title']


class SongAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAuthor
        # fields = "__all__"
        fields = ['name', 'long_desc', 'short_desc']
