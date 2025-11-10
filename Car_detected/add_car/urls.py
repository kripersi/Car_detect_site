from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_car, name='add_car'),
]

