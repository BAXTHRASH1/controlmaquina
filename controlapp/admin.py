from django.contrib import admin
from .models import Cliente,Usuario,Maquina,LogsMaquina
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Maquina)
admin.site.register(LogsMaquina)
