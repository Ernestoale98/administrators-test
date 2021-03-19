from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator

import json

from administrators.models import Administrator
from administrators.models import Rol


# Create your views here.


# Administrators


def index(request):
    query = request.GET['query']
    limit = request.GET['limit']
    page = request.GET['page']

    if query:
        data = Administrator.objects.filter(
            user__first_name__contains=query
        ).values(
            'pk',
            'user__first_name',
            'user__last_name',
            'user__email',
            'rol__name',
            'status'
        )
    else:
        data = Administrator.objects.all().values(
            'pk',
            'user__first_name',
            'user__last_name',
            'user__email',
            'rol__name',
            'status'
        )

    pagination = Paginator(list(data), limit)
    count = pagination.count
    pagination = pagination.page(page)

    response = {
        'data': pagination.object_list,
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
    administrator.rol_id = body['rol']
    administrator.save()
    administrator = Administrator.objects.filter(id=administrator.id).values(
        'pk',
        'user__first_name',
        'user__last_name',
        'user__email',
        'rol__id',
        'status'
    )
    return JsonResponse(list(administrator), safe=False)


def show(request, id):
    administrator = Administrator.objects.filter(id=id).values(
        'pk',
        'user__first_name',
        'user__last_name',
        'user__email',
        'rol__id',
        'status'
    )
    return JsonResponse(list(administrator), safe=False)


def update(request, id):
    body = json.loads(request.body)
    administrator = Administrator.objects.filter(id=id).first();
    # Update User
    user = administrator.user
    user.first_name = body['name']
    user.last_name = body['last_name']
    user.email = body['email']
    user.username = body['email']
    user.save()
    # Update administrator
    administrator.rol_id = body['rol']
    administrator.status = body['status']
    administrator.save()

    administrator = Administrator.objects.filter(id=id).values(
        'pk',
        'user__first_name',
        'user__last_name',
        'user__email',
        'rol__id',
        'status'
    )
    return JsonResponse(list(administrator), safe=False)


def destroy(request, id):
    administrator = Administrator.objects.filter(id=id).first();
    administrator.delete()
    return JsonResponse({
        'message': "Deleted"
    })


# Roles

def get_roles(request):
    data = Rol.objects.values('pk', 'name')
    response = {
        'data': list(data)
    }
    return JsonResponse(response, safe=False)
