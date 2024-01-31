from django.urls import path
from .views import index, student_details, home, about, calculate,notfound

urlpatterns = [
    path("", index, name="index"),
    path('student/<int:pk>', student_details, name="studentDetails"),
    path('home', home, name="home"),
    path('about', about, name="about"),
    path("calculate", calculate, name="calculate"),
    path("*", notfound, name="notfound")
]