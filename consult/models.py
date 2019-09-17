from django.db import models
from datetime import datetime

class Consult(models.Model):
    name = models.CharField(max_length = 5000, blank = True)
    email = models.CharField(max_length = 5000, blank = True)
    phone = models.CharField(max_length = 5000, blank = True)
    message = models.TextField(blank = True)
    description1 = models.TextField(blank = True)
    description2 = models.TextField(blank = True)
    description3 = models.TextField(blank = True)
    description4 = models.TextField(blank = True)
    description5 = models.TextField(blank = True)
    description6 = models.TextField(blank = True)
    date_sent = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.name 