from django.urls import path
from .views import createUser, getAllUser

urlpatterns = [
    path('create', createUser, name='createUser'),
    path('', getAllUser, name='getAllUser')
]