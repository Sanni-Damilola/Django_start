from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
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
