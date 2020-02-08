# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q
from .models import TangShi, TangAuthor


# from .models import Book
#
#
class BookFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """

    # pricemin = django_filters.CharFilter(name='updatestatus', help_text="完结",lookup_expr='gte')
    # pricemax = django_filters.CharFilter(name='shop_price', lookup_expr='lte')

    # top_category = django_filters.CharFilter(method='top_category_filter',lookup_expr='icontains')
    # def top_category_filter(self, queryset, name, value):
    #     return queryset.filter(Q(title=value) | Q(author=value))

    class Meta:
        model = TangShi
        fields = ['content']
        # fields = ['book__title', 'book__author','book__hot',
        #           'book__end_status', 'book__book_id','book__category']
