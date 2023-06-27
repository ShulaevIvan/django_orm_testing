from django.contrib import admin
from demo.models import Person, Car, Order, OrderPosition, Product

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']

class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderPositionInline]

