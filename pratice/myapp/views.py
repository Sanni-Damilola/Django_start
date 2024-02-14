from django.shortcuts import render
from .models import MyModel
from django.http import JsonResponse

# Create your views here.




def my_model_list(request):
    my_objects = MyModel.objects.all().values()
    return JsonResponse({"data": list(my_objects)})
