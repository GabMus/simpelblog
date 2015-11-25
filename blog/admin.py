from django.contrib import admin
from .models import Article, BlogPost, PagePost, Page

admin.site.register(PagePost)
admin.site.register(BlogPost)
admin.site.register(Page)
admin.site.register(Article)
