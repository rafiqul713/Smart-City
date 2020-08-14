from django.db import models

# Create your models here.

class StreetLight(models.Model):
    light_status = models.CharField(max_length = 10) #ON or OFF
    comment = models.CharField(max_length = 300) #particular problem, need to change etc
    def __str__(self):
         return "{} - {}".format(self.light_status, self.comment)

