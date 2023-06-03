from rest_framework import serializers
from .models import story

class storySerializer(serializers.ModelSerializer):
	class Meta:
		model = story
		fields = ['id', 'name', 'description']