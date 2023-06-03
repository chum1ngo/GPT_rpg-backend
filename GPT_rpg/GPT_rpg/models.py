from django.db import models

class story(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	# universe_name = models.CharField(max_length=200)
	# universe_context = models.CharField(max_length=2000)
	# universe_rules = models.CharField(max_length=200)
	# characters = models.CharField(max_length=2000)
	# characters_description = models.CharField(max_length=20000)
	# lore = models.CharField(max_length=20000000)
	
	def __str__(self):
		return self.name



		