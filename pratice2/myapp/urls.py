from  django.urls import path
from .views import getAllUsers, create, getOneUser, updateUser


urlpatterns = [
    path('', getAllUsers, name='getAllUsers'),
    path('create', create, name='create'),
    path('getoneuser/<int:pk>', getOneUser, name='getOneUser'),
    path('update/<int:pk>', updateUser, name='updateUser')
]