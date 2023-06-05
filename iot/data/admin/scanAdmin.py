from django.contrib import admin
from ..models.scan import Scan

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'time_register')
    search_fields = ['uuid', 'time_register']
    list_filter = ('uuid', 'time_register')
