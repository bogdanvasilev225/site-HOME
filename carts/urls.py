from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    path('cart_chande/<slug:product_slug>/', views.cart_chande, name='cart_chande'),
    path('cart_remove/<slug:product_slug>/', views.cart_remove, name='cart_remove'),
]


