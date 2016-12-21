from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username

class Category(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=128, unique=True)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)

		if self.likes < 0:
			self.likes = 0

		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.name

	class Meta:
        	verbose_name_plural = "categories"



class Page(models.Model):
	category = models.ForeignKey(Category)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField() #Only put something here if you want to specify something
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title
