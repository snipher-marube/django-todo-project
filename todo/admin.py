from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created']
    list_filter = ('completed', 'created')
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
