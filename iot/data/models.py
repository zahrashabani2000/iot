from django.db import models

class Scan(models.Model):
    uuid = models.IntegerField()
    time_register = models.DateTimeField(auto_now=True, db_column='timestamp')

    
    class Meta:
        ordering = ['-time_register']

    def __str__(self) -> str:
        return self.time_register
    
    def __repr__(self) -> str:
        return self.time_register
