from django.urls import path
from .views import index, student_details, home, about, calculate,notfound, result, Result, allStudent, studentUpdate, createStudent, getOneStudent, deleteStudent, teacherDetails, courseDetails

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
    path("student/<int:pk>/update", studentUpdate, name="studentUpdate"),
    path("student/<int:pk>/delete", deleteStudent, name="deleteStudent"),

    # Courses
    path("teacher/<int:teacherID>", teacherDetails, name="teacherDetails"),
    path("course/<int:courseID>", courseDetails, name="courseDetails")
]