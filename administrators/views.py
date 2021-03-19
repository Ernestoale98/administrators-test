from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers

import json

from administrators.models import Administrator
from administrators.models import Rol


# Create your views here.


# Administrators


def index(request):
    data = Administrator.objects.values(
        'pk',
        'user__first_name',
        'user__last_name',
        'user__email',
        'rol__name',
        'status'
    )
    count = Administrator.objects.count()
    response = {
        'data': list(data),
        'count': count
    }
    return JsonResponse(response, safe=False)


def store(request):
    body = json.loads(request.body)
    # Create User
    user = User.objects.create_user(
        username=body['email'],
        password=body['password']
    )
    user.email = body['email']
    user.first_name = body['name']
    user.last_name = body['last_name']
    user.save()
    # Create Administrator
    administrator = Administrator()
    administrator.user = user
    administrator.status = body['status']
    # Get Role
    role = Rol.objects.filter(id=body['rol']).first()
    administrator.rol = role
    administrator.save()
    data = serializers.serialize("json", [administrator])
    return HttpResponse(data, content_type="application/json")


# Roles

def get_roles(request):
    data = Rol.objects.values('pk', 'name')
    response = {
        'data': list(data)
    }
    return JsonResponse(response, safe=False)
