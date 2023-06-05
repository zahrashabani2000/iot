from django.db import models
from datetime import datetime


class Scan(models.Model):
    uuid = models.IntegerField()
    time_register = models.DateTimeField(auto_now=True, db_column='timestamp')

    
    class Meta:
        ordering = ['-time_register']

    def __str__(self):
        date_time = (self.time_register).timestamp()
        return str(date_time)

