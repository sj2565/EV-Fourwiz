from django.contrib import admin

#211007 추가
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import CarCharger

# Register your models here.
class CarChargerAdmin(ImportExportMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug':('area',)}

admin.site.register(CarCharger, CarChargerAdmin)