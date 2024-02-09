from django.urls import path
from .views import login, logout, signup

urlpatterns = [
    path("login", login),
    path("signup", signup),
    path("logout", logout),
]