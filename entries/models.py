from django.db import models
import datetime
# Create your models here.
class Entry(models.Model):
  date = models.DateField(default=datetime.date.today)
  purpose = models.CharField(max_length=255)
  time_on_task = models.IntegerField(default=0)
