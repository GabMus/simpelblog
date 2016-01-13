from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<page_id>[0-9]+)?$', views.index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/?$', views.post, name='post'),
    url(r'^post/(?P<post_id>[0-9]+)/postcomment/?$', views.postcomment, name='postcomment'),
    url(r'^page/(?P<page_name>.+)/?$', views.page, name='page'),
]
