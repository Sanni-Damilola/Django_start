from  django.urls import path
from .views import getAllUsers, create, getOneUser, updateUser, deleteUser


urlpatterns = [
    path('', getAllUsers, name='getAllUsers'),
    path('create', create, name='create'),
    path('getoneuser/<int:pk>', getOneUser, name='getOneUser'),
    path('update/<int:pk>', updateUser, name='updateUser'),
    path('deleteuser/<int:pk>', deleteUser, name='deleteUser')
]