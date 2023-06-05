from rest_framework import serializers
from .models import Story
from .models import Player
from .models import Character
from .models import Event
from .models import Trait
from .models import World
from .models import Rule

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ['id', 'name']

class StorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Story
		fields = ['id', 'player_id', 'name', 'description']

class CharacterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Character
		fields = ['id', 'player_id', 'story_id', 'name', 'description']


class TraitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trait
		fields = ['id', 'player_id', 'story_id', 'character_id', 'name', 'description']

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['id', 'player_id', 'story_id', 'character_id', 'sequence', 'description']

class WorldSerializer(serializers.ModelSerializer):
	class Meta:
		model = World
		fields = ['id', 'player_id', 'story_id', 'name', 'description']

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ['id', 'player_id', 'story_id', 'world_id', 'name', 'description']
