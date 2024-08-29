from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.Home.as_view(), name ='home'), # Mount the app's routes at the root URL
	path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('cars/<int:car_id>/add-cleaning/', views.add_cleaning, name='add-cleaning'),
    path('upgrades/create/', views.UpgradeCreate.as_view(), name='upgrade-create'),
    path('upgrades/<int:pk>/', views.UpgradeDetail.as_view(), name='upgrade-detail'),
    path('upgrades/', views.UpgradeList.as_view(), name='upgrade-index'),
    path('upgrades/<int:pk>/update/', views.UpgradeUpdate.as_view(), name='upgrade-update'),
    path('upgrades/<int:pk>/delete/', views.UpgradeDelete.as_view(), name='upgrade-delete'),
    path('cars/<int:car_id>/associate-upgrade/<int:upgrade_id>/', views.associate_upgrade, name='associate-upgrade'),
    path('cars/<int:car_id>/remove-upgrade/<int:upgrade_id>/', views.remove_upgrade, name='remove-upgrade'),
    path('accounts/signup/', views.signup, name='signup')
]