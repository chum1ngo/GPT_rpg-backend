from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name

class Story(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=1024)

	def __str__(self):
		return self.name
	
class Character(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=512)

	def __str__(self):
		return self.name
	
class Event(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
	sequence = models.IntegerField()
	description = models.CharField(max_length=1024)

	def __str__(self):
		return self.sequence
	
class Trait(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=512)

	def __str__(self):
		return self.name
	
class World(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=512)

	def __str__(self):
		return self.name
	
class Rule(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
	world_id = models.ForeignKey(World, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=512)

	def __str__(self):
		return self.name
	

		