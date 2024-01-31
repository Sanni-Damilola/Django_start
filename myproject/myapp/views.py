from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def student_details(request, pk):
    return HttpResponse(f"Details Page id of {pk}")

def home(request):
    return render(request, "home.html")