from django.db import models

# Create your models here.

class DairyMealBag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=15)

    def __str__(self):
        return self.name