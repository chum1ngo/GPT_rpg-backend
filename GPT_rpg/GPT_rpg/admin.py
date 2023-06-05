from django.contrib import admin
from .models import Story
from .models import Player
from .models import Character
from .models import Event
from .models import Trait
from .models import World
from .models import Rule

admin.site.register(Player)
admin.site.register(Story)
admin.site.register(Character)
admin.site.register(Trait)
admin.site.register(Event)
admin.site.register(World)
admin.site.register(Rule)