from django.urls import path
from .views import createUser

urlpatterns = [
    path('create', createUser, name='createUser')
]