from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=6, max_digits=10)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=6, max_digits=10)
    size = models.DecimalField(decimal_places=6, max_digits=10)
    description = models.CharField(max_length=100)
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer, related_name='games')

