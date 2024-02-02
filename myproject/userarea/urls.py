from django import path
from .views import register


urlpatterns = [
    path("register", register, name="register")
]