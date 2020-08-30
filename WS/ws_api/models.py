from django.db import models

# Create your models here.

class WeatherStation(models.Model):
    device_id= models.CharField(max_length =10,primary_key=True, serialize=True, verbose_name='device_id',null=False)
    sensor_name = models.CharField(max_length = 30)
    measurement_value = models.CharField(max_length = 10) # ON or OFF
    def __str__(self):
         return "{} - {}- {} ".format(self.device_id,self.sensor_name, self.measurement_value)
