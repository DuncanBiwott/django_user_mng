from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USER_NAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    service_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} in {self.organization.name}"

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)


# user = User.objects.get(username="username")
# service = Service.objects.get(name="specific_service")
# has_access = Subscription.objects.filter(
#     organization__membership__user=user, service=service, is_active=True
# ).exists()
