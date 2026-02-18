from django.db import models

# Create your models here.

class Service(models.Model):
    ServiceName = models.CharField(max_length=100)
    ServicePrice = models.IntegerField()
    ServiceStatus = models.BooleanField(default=True)
    Description = models.TextField
    discount = models.IntegerField()
    
    class Meta:
        db_table =" Service"
        
    def __str__(self):
        return self.ServiceName
