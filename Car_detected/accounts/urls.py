from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/<str:username>/', views.public_profile, name='public_profile'),
    path('car/<int:pk>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:pk>/delete/', views.delete_car, name='delete_car'),
]

