from django.urls import path
from . import views
app_name = 'app1'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
]