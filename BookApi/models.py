from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=40)
    author =models.CharField(max_length=40)
    # publishdate = models.DateField(blank=True, default='', null=True)
    publishdate = models.PositiveSmallIntegerField(blank=True, null=True)
    icon=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    infoLink=models.URLField(max_length=128, db_index=True, blank=True)