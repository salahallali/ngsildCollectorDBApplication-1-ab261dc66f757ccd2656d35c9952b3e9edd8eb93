from django.contrib import admin
from .models import Service
admin.site.site_header = 'Watermed Admin'
admin.site.register(Service)
