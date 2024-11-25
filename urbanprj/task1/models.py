from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.PositiveIntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    age_limited = models.BooleanField(default="False")
    buyer = models.ManyToManyField(Buyer, related_name='games')
