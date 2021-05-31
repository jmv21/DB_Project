from django.contrib import admin
from .models.Hunter import Hunter
from .models.Palico import Palico, Palico_lent
from .models.Monster import Monster
from .models.Object import Object, Collected_object, Armor, Weapon, Merchantable_Object
from .models.Element import Element, Elemental_resistance, Elemental_defense
from .models.Others import Recipes, Reward_object, Inventory
from .models.Element import Elemental_attack, Elemental_use


# Register your models here.
admin.site.site_header = "Administration site"
admin.site.site_title = "Monster Hunter administration"
admin.site.index_title = "Welcome to Monster Hunter's administration site"
admin.site.register(Hunter)
admin.site.register(Elemental_use)
admin.site.register(Elemental_attack)
admin.site.register(Palico)
admin.site.register(Monster)
admin.site.register(Object)
admin.site.register(Collected_object)
admin.site.register(Merchantable_Object)
admin.site.register(Armor)
admin.site.register(Weapon)
admin.site.register(Element)
admin.site.register(Elemental_defense)
admin.site.register(Elemental_resistance)
admin.site.register(Recipes)
admin.site.register(Reward_object)
admin.site.register(Inventory)
admin.site.register(Palico_lent)
