from django.urls import path
from .views import index, student_details, home

urlpatterns = [
    path("", index, name="index"),
    path('student/<int:pk>', student_details, name="studentDetails"),
    path('home', home, name="home")
]