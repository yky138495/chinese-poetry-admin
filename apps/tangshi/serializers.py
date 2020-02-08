from rest_framework import serializers
from django.db.models import Q
from .models import TangShi
from .models import TangAuthor


class TangShiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TangShi
        # fields = "__all__"
        fields = ['author', 'content', 'strains', 'title']


class TangAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TangAuthor
        # fields = "__all__"
        fields = ['name', 'long_desc', 'short_desc']
