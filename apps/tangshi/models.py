
from __future__ import unicode_literals

from django.db import models


class TangShi(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='id')
    id = models.AutoField(primary_key=True, verbose_name='编号')
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name='作者')
    content = models.CharField(unique=True, max_length=1000, verbose_name='内容')
    strains = models.CharField(max_length=1000, blank=True, null=True, verbose_name='平仄')
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='标题')

    class Meta:
        # managed = False
        verbose_name = '唐诗'
        verbose_name_plural = '唐诗'
        app_label = 'tangshi'
        db_table = 'tang_shi'

    def __str__(self):
        return "唐诗"

class TangAuthor(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # value = models.CharField(max_length=20, blank=True, null=True,unique=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True, verbose_name='作者名')
    long_desc = models.CharField(blank=True, null=True, max_length=5000, verbose_name='简介')
    short_desc = models.CharField(blank=True, null=True, max_length=5000, verbose_name='简介')

    class Meta:
        # managed = False
        verbose_name = '唐诗作者'
        verbose_name_plural = '唐诗作者'
        app_label = 'tangshi'
        db_table = 'tang_author'

    def __str__(self):
        return "唐诗作者"
