from django.contrib import admin
from ..models.scan import Scan

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    
    """
    Registers the scan model with the Django admin panel.

    Attributes:
        list_display: A tuple or list of field names to display in the admin's list view.
        search_fields: A tuple or list of field names to enable search functionality.
        list_filter: A tuple or list of field names to enable filtering of the scan records.

    Methods:
        N/A
    """
    list_display = ('id', 'uuid', 'time_register')
    search_fields = ['uuid', 'time_register']
    list_filter = ('uuid', 'time_register')
