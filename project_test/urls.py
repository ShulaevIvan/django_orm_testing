"""
URL configuration for project_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo.views import create_car
from demo.views import list_car
from demo.views import  create_person
from demo.views import list_persons

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newcar/', create_car),
    path('list_car/', list_car),
    path('create_person/', create_person),
    path('list_presons/', list_persons)
]
