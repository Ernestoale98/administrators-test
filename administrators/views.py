from django.http import JsonResponse
from django.core import serializers
import json

from administrators.models import Administrator


# Create your views here.

def index(request):
    data = Administrator.objects.values('pk', 'name', 'last_name', 'image', 'rol__name', 'status')
    count = Administrator.objects.count()
    response = {
        'data': list(data),
        'count': count
    }
    return JsonResponse(response, safe=False)
