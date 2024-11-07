from django.urls import path
from products.views import product_view, add_to_cart

urlpatterns = [
    path('<slug>/', product_view, name="product_view"),
    path('add-to-cart/<uid>/', add_to_cart, name="add_to_cart")
]