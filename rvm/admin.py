from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RVM

@admin.register(RVM)
class RVMAdmin(admin.ModelAdmin):
    list_display = ("machine_code", "location_name", "status", "last_usage_at", "created_at")
    list_filter = ("status", "location_name")
    search_fields = ("machine_code", "location_name")
    