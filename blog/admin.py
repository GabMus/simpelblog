from django.contrib import admin
from .models import Article, BlogPost, PagePost

admin.site.register(PagePost)
admin.site.register(BlogPost)
admin.site.register(Article)
