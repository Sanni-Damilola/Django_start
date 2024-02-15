from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import MyModel
from django.views.decorators.csrf import csrf_exempt


# Create your views here
@csrf_exempt
def createUser(req):

    if req.method == "POST":
        try:
            data = json.loads(req.body.decode('utf-8'))
        except json.JSONDecodeError:
            return HttpResponse("Invalid Json Data")
        
        name = data.get('name')
        description = data.get('description')

        if name and description:
            newUser = MyModel.objects.create(name=name, description=description)
            jsonData = {
                'id': newUser.pk,
                'name': newUser.name,
                'description': newUser.description
            }

            return JsonResponse (jsonData, status=201)
        else:
            return HttpResponse("Missing Required Fileds", status=400)
        
    else:
        return HttpResponse("Invaid Method For Request", status=405)


def getAllUser(req):
    if req.method == "GET":
        data = MyModel.objects.all().values()
        return JsonResponse({'data': list(data)})
    else:
        return HttpResponse("Invalid Request")


@csrf_exempt
def updateUser(req, pk):
    if req.method == "PATCH":
        try:
            data = json.loads(req.body.decode('utf-8'))
        
        except json.JSONDecodeError:
            return HttpResponse("Inavlid JSON data")
        
        try:
            my_model = MyModel.objects.get(pk=pk)
        except:
            return JsonResponse({'message': "Data Not Found"})
        
        name = data.get('name')
        description  = data.get('description')

        if name is not None:
            my_model.name = name
        if description is not None:
            my_model.description = description
        
        my_model.save()

        jsonData = {
            'id': my_model.pk,
            'name': my_model.name,
            'desciption': my_model.description
        }

        return JsonResponse(jsonData, status=200)
    else:
        HttpResponse('Invalid Method')


@csrf_exempt
def deleteAUser(req, pk):
    try:
        my_model = MyModel.objects.get(pk=pk)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Data Not Found'}, status= 404)
    
    if req.method == 'DELETE':
        my_model.delete()
        return JsonResponse({'message': 'User Deleted'})
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=405)

@csrf_exempt
def deleteAllUsers(req):
    if req.method == 'DELETE':
        MyModel.objects.all().delete()
        return JsonResponse({'message': 'Successfully Deleted All Users'})
    else:
        return JsonResponse({'error': 'Method Not Allowed'})


def handle404Route(req, exception):
    return JsonResponse({'error': f'This {req.path} Does Not Exist'}, status=404)
