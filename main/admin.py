from django.contrib import admin
from .models import ObjectMain, Managers

@admin.register(ObjectMain)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Managers)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'role')