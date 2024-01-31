from django.urls import path
from .views import index, student_details

urlpatterns = [
    path("", index, name="index"),
    path('student/<int:pk>', student_details, name="studentDetails")
]