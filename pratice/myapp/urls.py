from django.urls import path
from .views import my_model_list


urlpatterns = [
    path('', my_model_list, name="my_model_lost")
]