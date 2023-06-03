from django.http import JsonResponse
from .models import story
from .serializers import storySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(http_method_names=['GET','POST'])
def story_list(request):
	#get all the stories
	if request.method == 'GET':
		stories = story.objects.all()
		serializer = storySerializer(stories, many = True) 
		return JsonResponse({'stories':serializer.data}, safe=False)
	
	if request.method == 'POST':
		stories = story.objects.all()
		serializer = storySerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return
  