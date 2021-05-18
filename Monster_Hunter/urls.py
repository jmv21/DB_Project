from django.urls import path
from . import views

urlpatterns = [

    # ex: /Monster_Hunter/5/
    path('', views.home, name='home'),

    path('<int:number>/', views.rarest_objects, name='rarest_objects'),

    path('inventory/<int:number>/', views.inventory, name='inventory'),

    path('solidariest/', views.solidariest_palico, name='solidariest_palico'),

    path('hunters/', views.hunters, name='hunters'),

    path('palicos/', views.palicos, name='palicos'),

    path('objects/', views.objects, name='objects'),

    path('monsters/', views.monsters, name='monsters'),

    path('elements/', views.elements, name='elements'),

    path('solidariest_palico/', views.solidariest_palico, name='Spalico'),

    path('elements/<str:elements>/', views.elemental_resistant_armorset, name='armorset'),

    path('objects/details/<int:obj_id>/', views.object_details, name='object_detail'),

    path('monster/most_used_monster', views.most_popular_monster_equipment, name='most_popular_monster_equipment'),
]
