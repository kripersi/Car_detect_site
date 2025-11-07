from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

