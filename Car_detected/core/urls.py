from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('add_car/', include('add_car.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
