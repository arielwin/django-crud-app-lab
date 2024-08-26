from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

class Car:
    def __init__(self, make, model, description, year):
        self.make = make
        self.model = model
        self.description = description
        self.year = year

cars = [
    Car('Subaru', 'Outback', 'subaru outback limited awd 2.5l', 2022),
    Car('Toyota', 'Camry', 'toyota camry se awd nightshade', 2023),
    Car('Volvo', '740', 'Volvo 740 Wagon, 4spd manual', 1991),
    Car('Honda', 'Odyssey', 'Low and slow', 2001)
]

def car_index(request):
    return render(request, 'cars/index.html', { 'cars': cars})