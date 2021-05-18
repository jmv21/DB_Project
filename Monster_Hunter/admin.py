from django.contrib import admin
from .models.Hunter import Hunter
from .models.Palico import Palico
from .models.Palico import Palico_lent
from .models.Monster import Monster
from .models.Object import Object
from .models.Object import Collected_object
from .models.Object import Merchantable_Object
from .models.Object import Armor
from .models.Object import Weapon
from .models.Element import Element
from .models.Element import Elemental_defense
from .models.Element import Elemental_resistance
from .models.Others import Recipes
from .models.Others import Reward_object
from .models.Others import Inventory
from .models.Element import Elemental_attack


# Register your models here.
admin.site.register(Hunter)
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
