from django.urls import path
from .views import index, student_details, home, about, calculate,notfound, result, Result, allStudent, studentUpdate, createStudent, getOneStudent, deleteStudent

urlpatterns = [
    path("", index, name="index"),
    path('student/<int:pk>', student_details, name="studentDetails"),
    path('home', home, name="home"),
    path('about', about, name="about"),
    path("calculate", calculate, name="calculate"),
    path("*", notfound, name="notfound"),
    path("result", Result.as_view(), name="result"),

    # student (crud)
    path("student/create", createStudent, name="create_student"),
    path("student", allStudent, name="allStudent"),
    path("stuent/<int:pk>", getOneStudent, name="getOneStudent"),
    path("student/<int:pk>/delete", deleteStudent, name="deleteStudent"),
    path("update_student", studentUpdate, name="studentUpdate"),
    path("delete_student", deleteStudent, name="deleteStudent")
]