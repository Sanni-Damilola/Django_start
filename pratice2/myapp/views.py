from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def getAllUsers(req):
    if req.method == "GET":
        data = MyModel.objects.all()
        return JsonResponse({'data': list(data)})
    else:
        return JsonResponse({'error': "Invalid Method"})
    

def create(req):
