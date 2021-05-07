from django.urls import path
from . import views

urlpatterns = [

path('', views.hunters, name='hunters'),

# ex: /Monster_Hunter/5/
path('<int:number>/', views.rarest_objects, name='rarest_objects'),

path('solidariest/', views.solidariest_palico, name='solidariest_palico'),
]
