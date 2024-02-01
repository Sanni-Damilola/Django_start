from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.views import View
from .models import Student

# Create your views here.

# get all student
def allStudent(request):
    student = Student.objects.all()
    data = {
        "students": student
    }
    return render(request, "allStudent.html", data)

# get on student
def getOneStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = {
        "student": student
    }
    return render(request, "student_details.html",data)

# create student
def createStudent(request):
    if request.method == "POST":
        firstName = request.POST["first_name"]
        lastName = request.post["secondName"]
        age = request.POST["age"]
        bioGraphy = request.POST["bioGraphy"]

        Student.objects.create(
            firstName = firstName,
            lastName = lastName,
            age = age,
            bioGraphy = bioGraphy
        )

        return redirect("student_list")
    return render(request, "create_student.html")

# update student
def studentUpdate(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.firstName = request.POST["first_name"]
        student.lastName = request.post["secondName"]
        student.age = request.POST["age"]
        student.bioGraphy = request.POST["bioGraphy"]
        student.save()

        return redirect(request, "student_details", pk=pk)
    return render(request, "student_update.html", {"student": student})

# delet student
def deleteStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "delete_student.html", {"student": student})

class Result(View):
    def get(self, request):
     return HttpResponse("Not A Post Rquest")

    def post(self, request):
            first_num = request.POST["num1"]
            second_num = request.POST["num2"]
            op = request.POST["oprator"]
            op_match = {
                "plus": "+",
                "minus": "-",
                "divide": "/",
                "mutiply": "*"
            }
            data = f"{first_num}{op_match[op]}{second_num}"
            result = eval(data)
            context = {
                "result": result
            }
            return render(request, "result.html", context)  

def index(request):
    return render(request, "index.html")

def student_details(request, pk):
    return HttpResponse(f"Details Page id of {pk}")

def home(request):
    data = {
        'user': 'Sanni',
        'totalPoint': 400
    }
    return render(request, "home.html", data)

def about(request):
    return render(request, "about.html")

def calculate(request):
    return render(request, "calculate.html")

def notfound(request):
    print(request)


def result(request):
    if request.method == "POST":
        first_num = request.POST["num1"]
        second_num = request.POST["num2"]
        op = request.POST["oprator"]
        op_match = {
            "plus": "+",
            "minus": "-",
            "divide": "/",
            "mutiply": "*"
        }
        data = f"{first_num}{op_match[op]}{second_num}"
        result = eval(data)
        context = {
            "result": result
        }
        return render(request, "result.html", context)  
