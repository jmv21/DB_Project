from django.contrib import admin
from .models.Hunter import Hunter
from .models.Palico import Palico
from .models.Monster import Monster
from .models.Object import Object


# Register your models here.
admin.site.register(Hunter)
admin.site.register(Palico)
admin.site.register(Monster)
admin.site.register(Object)
