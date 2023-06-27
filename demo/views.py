from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from demo.models import Car, Person, Order
from .models import Weapon
from .serializers import WeaponSerializer
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


def list_orders(request):
    # context = {
    #     'orders': Order.objects.all()
    # }
    context = {
        'orders': Order.objects.filter(positions__product__price__lte=500)
        # 'orders': Order.objects.filter(positions__product__price__gte=500)
    }
    return render(request, 'orders.html', context)

# @api_view(['GET', 'POST'])
# def demo_api(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
    
#     if request.method == 'POST':
#         print(request)
#         return Response({'status': 'ok'})


# class Demo_api(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     def post(self, request):
#         print(request)
#         return Response({'status': 'ok'})

# class DemoApi(ListAPIView):
#     queryset = Weapon.objects.all()
#     serializer_class = WeaponSerializer

#     def post(self, request):
#         return Response({'status': 'ok'})



class DemoApi(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer