from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import TangShi, TangAuthor
from .serializers import TangShiSerializer, TangAuthorSerializer


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
class TangShiListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = TangShi.objects.all()
    serializer_class = TangShiSerializer
    pagination_class = BooksPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# CacheResponseMixin,
class TangAuthorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = TangAuthor.objects.all()
    serializer_class = TangAuthorSerializer
    pagination_class = ChapterPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
