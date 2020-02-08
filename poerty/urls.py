"""poerty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf.urls import url,include
import xadmin
from .settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from tangshi.views import TangShiListViewSet, TangAuthorViewSet
from songshi.views import SongShiListViewSet, SongAuthorViewSet


router = DefaultRouter()
router.register(r'tang_shi', TangShiListViewSet, base_name="tang_shi")
router.register(r'tang_author', TangAuthorViewSet, base_name="tang_author")
router.register(r'song/shi', SongShiListViewSet, base_name="song_shi")
router.register(r'song/author', SongAuthorViewSet, base_name="song_author")


from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'docs/', include_docs_urls(title="文档")),

    # drf自带的token认证模式
    # url(r'^api-token-auth/', views.obtain_auth_token),
    #
    # # jwt的认证接口
    # url(r'^login/', obtain_jwt_token),
]