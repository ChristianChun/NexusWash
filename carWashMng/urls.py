# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('services', views.service_s, name='services'),
    path('bookings', views.booking_list, name='booking_list'),  # URL for booking list
    path('bookings/new', views.booking_create, name='booking_create'),
    path('profile', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile'),
    path('check_availability', views.check_availability, name='check_availability'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
