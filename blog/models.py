from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
#Category
class Dj_category(models.Model):
	category_name = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)
	category_description = models.TextField()

	def  __str__(self):
		return self.category_name

#User´s posts
class Dj_post(models.Model):
	post_author = models.ForeignKey(User)
	post_category_id = models.ForeignKey(Dj_category,on_delete=models.CASCADE, null=True)
	post_date = models.DateTimeField(default=datetime.now, blank=True)
	post_title = models.CharField(max_length=150)
	post_content = models.TextField()
	comment_count = models.IntegerField()
	post_type = models.CharField(max_length=20)
	post_modified = models.DateField()

	def __str__(self):
		return self.post_title

#Comments of the posts
class Dj_comments(models.Model):
	comment_post_ID = models.ForeignKey(Dj_post)
	comment_content = models.TextField()
	comment_approved = models.CharField(max_length=20)
	comment_type = models.CharField(max_length=20)
	comment_date = models.DateField()
	comment_author_IP = models.CharField(max_length=200)
	comment_author_URL = models.URLField()
	comment_author_email = models.CharField(max_length=100)
	user_ID = models.IntegerField()

	def __str__():
		return self.comment_author_email