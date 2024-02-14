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