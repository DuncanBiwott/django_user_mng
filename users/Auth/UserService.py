import json
from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse


class UserService:
    def create_user(self,request):
        try:
            if request.method == "POST":
                data = json.loads(request.body)
                user_name = data.get("username")
                email = data.get("email")
                password = data.get("password")
                saved_user=User.objects.create_user(user_name, email, password)
                if saved_user:
                    return JsonResponse({"message":"User created Successfully"})
            else:
                return JsonResponse({"message":"Invalid request"})
        except IntegrityError as e:
            return f"Error creating user: {str(e)}"

    def login_user(self,request):
        try:
            if request.method == "POST":
                data = json.loads(request.body)
                user_name = data.get("username")
                password = data.get("password")
                user=authenticate(request,username=user_name,password=password)
                if user is not None:
                    login(request, user)
                    print("User logged in")
                    return JsonResponse({"message": {"username": user.get_username(), "email": user.email}})
                else:
                    return JsonResponse({"message":"Invalid credentials"})
            else:
                return JsonResponse({"message":"Invalid request"})
        except Exception as e:
            return JsonResponse({"message":"User does not exist"})

    def logout_user(self,request):
        try:
            logout(request)
            return JsonResponse({"message":"Logged out"})
        except Exception as e:
            return JsonResponse({"message":str(e)})
    def get_user(self,request,id):
        try:
            if request.user.is_authenticated:
                user=User.objects.get(id=id)
                if user is None:
                    return JsonResponse({"message":"User does not exist"})
                else:
                    return JsonResponse({"message":{"username":user.get_username(),"email":user.email}})
            else:
                return JsonResponse({"message":"User not logged in"})
        except Exception as e:
            return JsonResponse({"message":str(e)})

    def reset_password(self,request):
        try:
            if request.method == "POST":
                data = json.loads(request.body)
                user_name = data.get("username")
                password = data.get("password")
                user=User.objects.get(username=user_name)
                if user is None:
                    return JsonResponse({"message":"User does not exist"})
                else:
                    user.set_password(password)
                    user.save()
                    return JsonResponse({"message":"Password reset successfully"})
            else:
                return JsonResponse({"message":"Invalid request"})
        except Exception as e:
            return JsonResponse({"message":str(e)})







