from  django.urls import path
from .views import getAllUsers, create


urlpatterns = [
    path('', getAllUsers, name='getAllUsers'),
    path('create', create, name='create')
]