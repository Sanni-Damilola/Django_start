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