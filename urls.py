from django.urls import path
from . import views

urlpatterns = [
    path('', views.dairy_meal_bag_list, name='dairy_meal_bag_list'),
    path('create/', views.create_dairy_meal_bag, name='create_dairy_meal_bag'),
    path('update/<int:pk>/', views.update_dairy_meal_bag, name='update_dairy_meal_bag'),
    path('delete/<int:pk>/', views.delete_dairy_meal_bag, name='delete_dairy_meal_bag'),
    path('clients/', views.clients, name='clients'),
]