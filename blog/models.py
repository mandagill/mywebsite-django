from django.db import models
from django.utils import timezone


class BlogPost(models.Model):  #models.Model tells Django this is a model and needs to be saved to the db
	author = models.ForeignKey('auth.User') #This is a link to another model
	title = models.CharField(max_length=200)
	text = models.TextField()  #No max char length
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True) #If no date specified, defaults to nothing?


	def publish(self):
		self.published_date = timezone.now() #Doesn't change *state* of object, just assigns a published date. 
		self.save()


	def __str__(self):
		return self.title