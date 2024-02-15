from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getAllUsers(req):
    if req.method == "GET":
        data = MyModel.objects.all().values()
        if len(data) != 0:
            return JsonResponse({'data': list(data)})
        else:
            return JsonResponse({'message': 'No User Avaliable'})
    else:
        return JsonResponse({'error': "Invalid Method"})
    

@csrf_exempt
def create(req):
    if req.method == "POST":
        try:
            model = json.loads(req.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Expected Json Data'}, status=400)
        
        name = model.get('name')
        age = model.get('age')
        if name and age:
            newUser = MyModel.objects.create(name=name, age=age)
            data = {
                'id': newUser.pk,
                'name': newUser.name,
                'age': newUser.age
            }
            return JsonResponse(data, status=201)
        else:
            return JsonResponse({'error': 'Field is Required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=405)


# def