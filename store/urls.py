from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product-list/', views.product_list, name='product_list'),
    path('single-product/', views.single_product, name='single_product'),
]
