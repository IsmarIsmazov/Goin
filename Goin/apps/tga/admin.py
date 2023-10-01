from django.contrib import admin

from .models import Admin
from .forms import AdminForm

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "name")
    form = AdminForm
