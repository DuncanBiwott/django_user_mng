import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data=json.loads(request.body)
        user_name = data.get("username")
        email = data.get("email")
        password = data.get("password")
        saved_user = User.objects.create_user(user_name,email,password)
        saved_user.save()
        return JsonResponse({"data":{"username":user_name,"email":email}})
    else:
        return JsonResponse({"message":"Hello, world. You're at the users index."})

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"message":"Logged out"})

@csrf_exempt
def login_user(request):
    print(request)
    data=json.loads(request.body)
    user_name = data.get("username")
    password = data.get("password")
    user=authenticate(request,username=user_name,password=password)
    if user is not None:
        login(request,user)
        print("User logged in")
        return JsonResponse({"message":{"username":user.get_username(),"email":user.email}})
    else:
        return JsonResponse({"message":"Invalid credentials"})