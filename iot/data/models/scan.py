from django.db import models
from django.utils.translation import gettext_lazy as _

class Scan(models.Model):
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