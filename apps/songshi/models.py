# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class SongShi(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='id')
    id = models.AutoField(primary_key=True, verbose_name='编号')
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name='作者')
    content = models.CharField(unique=True,max_length=1000, verbose_name='内容')
    strains = models.CharField(max_length=1000,blank=True, null=True, verbose_name='平仄')
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='标题')

    class Meta:
        verbose_name = '宋诗'
        verbose_name_plural = '宋诗'
        managed = False
        app_label = 'songshi'  # 这里需要对应app的名
        db_table = 'shi'

    def __str__(self):
        return "宋诗"

class SongAuthor(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # value = models.CharField(max_length=20, blank=True, null=True,unique=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True, verbose_name='作者名')
    long_desc = models.CharField(blank=True, null=True,max_length=5000, verbose_name='简介')
    short_desc = models.CharField(blank=True, null=True,max_length=5000, verbose_name='简介')

    class Meta:
        verbose_name = '宋诗作者'
        verbose_name_plural = '宋诗作者'
        managed = False
        app_label = 'songshi'
        db_table = 'author'

    def __str__(self):
        return "宋诗作者"
