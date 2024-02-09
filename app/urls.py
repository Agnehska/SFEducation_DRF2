from django.urls import path
from .views import get_products, post_products, update_product, update_cart, get_cart, order

urlpatterns = [
    path("products", get_products),
    path("product", post_products),
    path("product/<int:pk>", update_product),

    path("cart", get_cart),
    path("cart/<int:pk>", update_cart),

    path("order", order)
]