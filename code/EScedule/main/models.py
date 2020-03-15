from django.db import models
from datetime import datetime
# Create your models here.
class Lesson(models.Model):
    name = models.TextField(null=False, default=None)
    day = models.IntegerField(null=False, default=None)
    time = models.TimeField()
    hometask = models.TextField(default='')
    is_done = models.BooleanField(default=False)
    note = models.TextField(default='')
