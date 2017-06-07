from django.db import models
from ckeditor.fields import RichTextField

class Story(models.Model):
	title = models.CharField(max_length = 250)
	body = models.TextField()
	
	def __str__(self):
		return self.tag_name
# Create your models here.
'''class Author(models.Model):
	# Define the blog authhor table
	name= models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	bio = models.TextField()

	def __str__(self):
		return self.name

class Category(models.Model):
	#Define the blog category table
	cat_name = models.CharField('Category Name',max_length=50)
	cat_descriptio = models.CharField('Category Description',max_length=255)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.cat_name

class Tag(models.Model):
	#Define the blog tag table
	tag_name = models.CharField(max_length=50)
	tag_description = models.CharField(max_length = 255)



	def __str__(self):
		return self.tag_name


class Post(models.Model):
	# Define the blog Post table
	title= models.CharField(max_length = 200)
	body = RichTextField(('shrawan'))
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title '''