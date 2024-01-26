import json

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == "POST":
        data=json.loads(request.body)
        user_name = data.get("username")
        email = data.get("email")
        password = data.get("password")
        saved_user = User.objects.create_user(user_name,email,password)
        print(saved_user)
        return JsonResponse({"data":{"username":user_name,"email":email,"password":password}})
    else:
        return JsonResponse({"message":"Hello, world. You're at the users index."})


def logout(request):
    return JsonResponse({"message":"Hello, world. You're at the users index."})


def login(request):
    return JsonResponse({"message":"Hello, world. You're at the users index."})