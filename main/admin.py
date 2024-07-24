from django.contrib import admin
from .models import ObjectMain

@admin.register(ObjectMain)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')