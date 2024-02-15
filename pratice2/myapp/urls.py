from  django.urls import path
from .views import getAllUsers


urlpatterns = [
    path('', getAllUsers, name='getAllUsers')
]