from django.db import models
from datetime import datetime

class About(models.Model):
    title = models.CharField(max_length = 5000, blank = True)
    sub_title = models.CharField(max_length = 5000, blank = True)
    about1 = models.TextField(blank = True)
    about2 = models.TextField(blank = True)
    sub_title2 = models.CharField(max_length = 5000, blank = True)
    about3 = models.TextField(blank = True)
def __str__(self):
    return self.title 