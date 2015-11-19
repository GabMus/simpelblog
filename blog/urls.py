from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<page_id>[0-9]+)?$', views.index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^pages/(?P<page_name>.+)$', views.page, name='page'),
]
