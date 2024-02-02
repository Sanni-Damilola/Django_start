from django.urls import path
from .views import archive, details


urlpatterns = [
    path("", archive, name="archive"),
    path("detail/<int:pk>", details, name="details")
]