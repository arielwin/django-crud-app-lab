from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name ='home'), # Mount the app's routes at the root URL
	path('cars/', views.car_index, name='car-index'),
]