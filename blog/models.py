from django.db import models

class Article(models.Model):
    posttitle = models.TextField(default="Post")
    post = models.TextField()
    piclink = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class BlogPost(Article):
    def __str__(self):
        return self.posttitle

class PagePost(Article):
    tag = models.CharField(default="default", max_length=150)

    def __str__(self):
        return self.tag+" "+self.posttitle
