from django.urls import path
from . import views

urlpatterns = [
    # ex: /Monster_Hunter/5/
    path('', views.home, name='home'),

    path('<int:number>/', views.rarest_objects, name='rarest_objects'),

    path('inventory/<int:number>/', views.inventory, name='inventory'),

    path('solidariest/', views.solidariest_palico, name='solidariest_palico'),

    path('hunters/', views.hunters, name='hunters'),

    path('palicos/', views.palicos, name='palicoes'),

    path('objects/', views.objects, name='objects'),

    path('monsters/', views.monsters, name='monsters'),

    path('elements/', views.elements, name='elements'),

    path('solidariest_palico/', views.solidariest_palico, name='solidariest_palico'),

    path('elements/<str:elements>/', views.elemental_resistant_armorset, name='armorset'),

    path('objects/details/<int:obj_id>/', views.object_details, name='object_detail'),

    path('monster/most_used_monster', views.most_popular_monster_equipment, name='most_popular_monster_equipment'),

    path('monsters/most_resistant_armor/<int:monster>/', views.resistent_armor, name='resistent_armor'),

    path('monster_to_kill/<int:equipment_id>/', views.monsters_to_kill, name='resistent_armor'),

    path('palicoes/lend_register/', views.lend_register, name='lend_register'),

    path('object/recipe/<int:id>', views.recipe, name='lend_register'),
]
