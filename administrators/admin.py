from django.contrib import admin

from administrators.models import Administrator
from administrators.models import Rol
# Register your models here.
admin.site.register(Administrator)
admin.site.register(Rol)
