#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import TangShi, TangAuthor


class TangShiAdmin(object):
    list_display = ["id", "author", "content", "strains", "title"]
    search_fields = ["id", "content", "content", "strains", "title"]
    list_editable = ["content", "content", "strains", "title"]
    list_filter = ["content", "content", "strains", "title"]


class TangAuthorAdmin(object):
    list_display = ["id", "name", "long_desc", "short_desc"]
    search_fields = ["id", "name", "long_desc", "short_desc"]
    list_editable = ["name", "long_desc", "short_desc"]
    list_filter = ["id", "name", "long_desc", "short_desc"]


xadmin.site.register(TangShi, TangShiAdmin)
xadmin.site.register(TangAuthor, TangAuthorAdmin)
