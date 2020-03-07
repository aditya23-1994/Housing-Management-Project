from django.contrib import admin
from .models import Inquiry

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'issue','email','contact_date','resolve']
    list_display_links = ['id','name']
    search_fields = ['name','email','issue']

    list_per_page = 25

admin.site.register(Inquiry,ContactAdmin)
