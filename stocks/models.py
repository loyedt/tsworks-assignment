from django.db import models

# Create your models here.
class Stockval(models.Model):
    date=models.CharField(max_length=20)
    open=models.CharField(max_length=20)
    high=models.CharField(max_length=20)
    low=models.CharField(max_length=20)
    close=models.CharField(max_length=20)
    adj_close=models.CharField(max_length=20)
    volume=models.CharField(max_length=20)

