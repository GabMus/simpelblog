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
	parentpage = models.ForeignKey('Page', null=True)

	def __str__(self):
		return self.tag+" "+self.posttitle
		
class Page(models.Model):
	page_index = models.IntegerField(default=0)
	name = models.CharField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name

class Comment(models.Model):
	name=models.CharField(max_length=20, blank=False)
	email=models.CharField(max_length=120, blank=False)
	text=models.CharField(max_length=512, blank=False)
	parent_article=models.ForeignKey('BlogPost', null=False)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email+" "+self.parent_article.__str__()
