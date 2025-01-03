from django.contrib import admin
from graph.models import Data
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title','content')