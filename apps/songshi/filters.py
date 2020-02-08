# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q
from .models import SongShi, SongAuthor


# from .models import Book
#
#
class BookFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """

    # top_category = django_filters.CharFilter(method='top_category_filter',lookup_expr='icontains')
    # def top_category_filter(self, queryset, name, value):
    #     return queryset.filter(Q(title=value) | Q(author=value))

    class Meta:
        model = SongShi
        fields = ['id']
        # fields = ['book__title', 'book__author','book__hot',
        #           'book__end_status', 'book__book_id','book__category']
