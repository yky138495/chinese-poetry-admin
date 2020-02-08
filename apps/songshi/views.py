from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import SongShi, SongAuthor
from .serializers import SongShiSerializer, SongAuthorSerializer


# Create
# Create your views here.

class BooksPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ChapterPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


# CacheResponseMixin
class SongShiListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = SongShi.objects.all()
    serializer_class = SongShiSerializer
    pagination_class = BooksPagination

# CacheResponseMixin,
class SongAuthorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = SongAuthor.objects.all()
    serializer_class = SongAuthorSerializer
    pagination_class = ChapterPagination