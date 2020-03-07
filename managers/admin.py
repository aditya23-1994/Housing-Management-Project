from django.contrib import admin
from .models import Manager,Worker

class ManageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','designation', 'phone', 'email', 'is_available')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_available',)
    search_fields = ('id','name','designation','phone')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'work', 'manager', 'phone','is_availabe', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'manager')
    list_editable = ('is_availabe',)
    search_fields = ('id','name','work','phone','manager')

admin.site.register(Manager,ManageAdmin)
admin.site.register(Worker,WorkerAdmin)
