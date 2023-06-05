from django.http import JsonResponse

from .models import Story
from .models import Player
from .models import Character
from .models import Event
from .models import Trait
from .models import World
from .models import Rule

from .serializers import StorySerializer
from .serializers import PlayerSerializer
from .serializers import CharacterSerializer
from .serializers import TraitSerializer
from .serializers import EventSerializer
from .serializers import WorldSerializer
from .serializers import RuleSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


######  PLAYER METHODS  ######
@api_view(http_method_names=['GET','POST'])
def player_list(request, format=None):
	#get all the stories
	if request.method == 'GET':
		players = Player.objects.all()
		serializer = PlayerSerializer(players, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		players = Player.objects.all()
		serializer = PlayerSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def player_detail(request, id, format=None):
	try:
		player = Story.objects.get(pk=id)
	except player.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = PlayerSerializer(player)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = PlayerSerializer(player, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		player.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  STORY METHODS  ######
@api_view(http_method_names=['GET','POST'])
def story_list(request, format=None):
	#get all the stories
	if request.method == 'GET':
		stories = Story.objects.all()
		serializer = StorySerializer(stories, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		stories = Story.objects.all()
		serializer = StorySerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def story_detail(request, id, format=None):
	try:
		story = Story.objects.get(pk=id)
	except story.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = StorySerializer(story)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = StorySerializer(story, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		story.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  world METHODS  ######
@api_view(http_method_names=['GET','POST'])
def world_list(request, format=None):
	
	if request.method == 'GET':
		worlds = World.objects.all()
		serializer = WorldSerializer(worlds, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		worlds = World.objects.all()
		serializer = WorldSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def world_detail(request, id, format=None):
	try:
		world = World.objects.get(pk=id)
	except world.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = WorldSerializer(world)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = WorldSerializer(world, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		world.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  rule METHODS  ######
@api_view(http_method_names=['GET','POST'])
def rule_list(request, format=None):
	
	if request.method == 'GET':
		rules = Rule.objects.all()
		serializer = RuleSerializer(rules, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		rules = Rule.objects.all()
		serializer = RuleSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def rule_detail(request, id, format=None):
	try:
		rule = Rule.objects.get(pk=id)
	except rule.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = RuleSerializer(rule)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = RuleSerializer(rule, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		rule.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  trait METHODS  ######
@api_view(http_method_names=['GET','POST'])
def trait_list(request, format=None):
	
	if request.method == 'GET':
		traits = Trait.objects.all()
		serializer = TraitSerializer(traits, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		traits = Trait.objects.all()
		serializer = TraitSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def trait_detail(request, id, format=None):
	try:
		trait = Trait.objects.get(pk=id)
	except trait.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = TraitSerializer(trait)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = TraitSerializer(trait, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		trait.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  character METHODS  ######
@api_view(http_method_names=['GET','POST'])
def character_list(request, format=None):
	
	if request.method == 'GET':
		characters = Character.objects.all()
		serializer = CharacterSerializer(characters, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		characters = Character.objects.all()
		serializer = CharacterSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def character_detail(request, id, format=None):
	try:
		character = Character.objects.get(pk=id)
	except character.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = CharacterSerializer(character)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = CharacterSerializer(character, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		character.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return

######  event METHODS  ######
@api_view(http_method_names=['GET','POST'])
def event_list(request, format=None):
	
	if request.method == 'GET':
		events = Event.objects.all()
		serializer = EventSerializer(events, many = True) 
		return Response(serializer.data)
	
	if request.method == 'POST':
		events = Event.objects.all()
		serializer = EventSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  
@api_view(http_method_names=['GET','PUT','DELETE'])
def event_detail(request, id, format=None):
	try:
		event = Event.objects.get(pk=id)
	except event.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = EventSerializer(event)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = EventSerializer(event, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		event.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return