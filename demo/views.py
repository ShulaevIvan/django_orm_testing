from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Car, Person
import random

# Create your views here.

def create_car(request):
    car = Car(brand=random.choice(['b1','b2','b3']), model=random.choice(['m1','m2','m3']), color=random.choice(['c1','c2','c3']))
    car.save()
    return HttpResponse(f'car created {car.brand} {car.model}')


def list_car(request):
    # car_objects = Car.objects.all()
    # car_objects = Car.objects.filter(brand='b1')
    # car_objects = Car.objects.filter(brand__contains='1')
    car_objects = Car.objects.filter(brand__startswith='b')
    cars = [f'{c.id} {c.brand} {c.model} {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name = 'P', car = car)
    return HttpResponse('created')


def list_persons(request):
    persons_objects = Person.objects.all()
    persons = [f'{p.name}, {p.car}' for p in persons_objects] 
    return HttpResponse('<br>'.join(persons))