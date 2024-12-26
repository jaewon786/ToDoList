from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
  search_fields = ['content']
  
admin.site.register(Todo, TodoAdmin)
