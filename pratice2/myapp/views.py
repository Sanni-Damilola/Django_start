from django.shortcuts import render, get_list_or_404
from .models import MyModel
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

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


@csrf_exempt
def getOneUser(request, pk):
    
    if request.method == "GET":
        try:
            user = MyModel.objects.get(pk=pk)
            data = {
                'id': user.pk,
                'name': user.name,
                'age': user.age
            }
            return JsonResponse(data)
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=405)
    

@csrf_exempt
def updateUser(req, pk):
    if req.method == "PATCH":
        try:
            model = json.loads(req.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Expected Json Data'}, status=400)
        
        try:
            my_model = MyModel.objects.get(pk=pk)
        except:
            return JsonResponse({'error': 'User Not Found'}, status=404)
    

        name = model.get('name')
        age = model.get('age')

        if name is not None or age is not None:
            my_model.name = name
            my_model.age = age
        
        my_model.save()
        data = {
            'id': my_model.pk,
            'name': my_model.name,
            'age': my_model.age
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=405)


@csrf_exempt
def deleteUser(req, pk):
    try:
        my_model = MyModel.objects.all().get(pk=pk)
    except: 
        return JsonResponse({'error': 'User Not Found'}, status=404)

    if req.method == "DELETE":
        my_model.delete()
        return JsonResponse({'message': 'User Deleted'})
    else:
        return JsonResponse({'error': 'Method Not Allowed'})
