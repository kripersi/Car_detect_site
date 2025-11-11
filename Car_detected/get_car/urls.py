from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_car, name='search_car'),
    path('car/<int:pk>/', views.car_detail, name='car_detail')
]

