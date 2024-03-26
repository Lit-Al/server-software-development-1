from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'completed', 'priority')
    list_filter = ('completed', 'priority')
    search_fields = ('title',)
    date_hierarchy = 'deadline'
