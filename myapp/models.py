from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=200, help_text="enter a genre name")

	def __str__(self):
		return self.name

class Image(models.Model):
	imageName = models.CharField(max_length=200, help_text="enter an image name")
	genre = models.ManyToManyField(Genre, help_text="select a genre for this image")
	date = models.DateField(null=False, blank=False)

	class Meta:
		ordering = ['imageName']

	def get_absolute_url(self):
		return reverse('image-detail', args=[str(self.id)])

	def display_genre(self):
		return ', '.join([ genre.name for genre in self.genre.all()])

	display_genre.short_description = 'Genre'

	def __str__(self):
		return self.imageName