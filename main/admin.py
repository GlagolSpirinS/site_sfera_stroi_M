from django.contrib import admin
from .models import ObjectMain, Managers, Jobs

@admin.register(ObjectMain)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Managers)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'role')

@admin.register(Jobs)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'trebuyemyy_opyt_raboty', 'zanyatost', 'grafik', 'udalonnayarabota', 'mesto_raboty')
