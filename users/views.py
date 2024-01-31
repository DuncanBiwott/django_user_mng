
from django.views.decorators.csrf import csrf_exempt
from .Auth import UserService


@csrf_exempt
def register_user(request):
    response = UserService().create_user(request)
    return response

@csrf_exempt
def logout_user(request):
    response = UserService().logout_user(request)
    return response

@csrf_exempt
def login_user(request):
    response = UserService().login_user(request)
    return response
@csrf_exempt
def get_user(request,id):
    response = UserService().get_user(request,id)
    return response