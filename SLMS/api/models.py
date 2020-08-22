from django.db import models

# Create your models here.

class StreetLight(models.Model):
    device_id= models.CharField(max_length =10,primary_key=True, serialize=True, verbose_name='device_id',null=False)
    light_status = models.CharField(max_length = 10) # ON or OFF
    def __str__(self):
         return "{} - {}".format(self.device_id,self.light_status)

