from django.urls import path

from . import views

app_name = 'tickets'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('', views.ticketform, name='ticketform'),
   
]