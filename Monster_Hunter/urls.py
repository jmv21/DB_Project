from django.urls import path
from . import views

urlpatterns = [

    # ex: /Monster_Hunter/5/
    path('', views.home, name='home'),

    path('<int:number>/', views.rarest_objects, name='rarest_objects'),

    path('solidariest/', views.solidariest_palico, name='solidariest_palico'),

    path('hunters/', views.hunters, name='hunters'),

    path('palicos/', views.palicos, name='palicos'),

    path('objects/', views.objects, name='objects'),

]
