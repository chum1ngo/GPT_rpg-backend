"""
URL configuration for GPT_rpg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GPT_rpg import views
from rest_framework.urlpatterns import format_suffix_patterns

# CAMBIAR AQUI URL PARA DESPUES
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('story/', views.story_list),
    path('story/<int:id>', views.story_detail),
    
		path('player/', views.player_list),
		path('player/<int:id>', views.player_detail),
        
		path('character/', views.character_list),
		path('character/<int:id>', views.character_detail),
        
		path('trait/', views.trait_list),
		path('trait/<int:id>', views.trait_detail),
        
		path('event/', views.event_list),
		path('event/<int:id>', views.event_detail),
      
		path('world/', views.world_list),
		path('world/<int:id>', views.world_detail),
        
		path('rule/', views.rule_list),
		path('rule/<int:id>', views.rule_detail),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
