from django.contrib import admin
from .models import Article, BlogPost, PagePost, Page, Comment

admin.site.register(PagePost)
admin.site.register(BlogPost)
admin.site.register(Page)
admin.site.register(Article)
admin.site.register(Comment)
