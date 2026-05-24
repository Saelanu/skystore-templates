from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)