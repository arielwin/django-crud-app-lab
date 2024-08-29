from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Upgrade(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('upgrade-detail', kwargs={'pk': self.id})
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    warranty = models.BooleanField()
    color = models.CharField(max_length=100)
    upgrades = models.ManyToManyField(Upgrade)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id' : self.id })
    


TYPES = (
    ('X', 'Exterior'),
    ('I', 'Interior'),
    ('W', 'Wheels'),
    ('F', 'Full Service')
)
class Cleaning(models.Model):
    date = models.DateField('Washed on')
    type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
