from django.urls import path
from .views import createUser, getAllUser,updateUser

urlpatterns = [
    path('create', createUser, name='createUser'),
    path('', getAllUser, name='getAllUser'),
    path('update/<int:pk>', updateUser, name='updateUser')
]