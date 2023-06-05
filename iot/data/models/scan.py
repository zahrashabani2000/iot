from django.db import models
from django.utils.translation import gettext_lazy as _

class Scan(models.Model):
    
    """Defines a scan record in the database.

    Attributes:
        uuid (int): The unique identifier of the scan.
        time_register (datetime): The timestamp when the scan was registered.

    Meta:
        ordering: A list or tuple of model field names used for ordering the query results.
        verbose_name: A human-readable name for the model.
        verbose_name_plural: A human-readable plural name for the model.

    Methods:
        __str__: Returns a string representation of the scan record.
        __repr__: Returns a string representation of the scan record.

    """
    
    uuid = models.IntegerField(
        verbose_name=_('Uuid')
    )
    time_register = models.DateTimeField(
        auto_now=True, 
        db_column='timestamp', 
        verbose_name=_('Timestamp')
    )

    class Meta:
        ordering = ['-time_register']
        verbose_name = _('scan')
        verbose_name_plural = _('scans')

    def __str__(self) -> str:
        return str(self.time_register)
    
    def __repr__(self) -> str:
        return str(self.time_register)