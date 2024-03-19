from django.db import models

# Create your models here.
class Stocks(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    sectors = models.CharField(max_length=100)
    holding = models.FloatField()
    fname = models.CharField(max_length=100)
    ftype = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.sname}'