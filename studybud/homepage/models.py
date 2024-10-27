from django.db import models
import datetime

# Create your models here.
class posts(models.Model):
    ttext=models.CharField(max_length=200 )
    timee=models.TimeField(default=str(datetime.datetime.now()))
    def __str__(self):
        return str(self.timee)
    