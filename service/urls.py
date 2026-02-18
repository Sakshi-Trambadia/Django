from django.urls import path
from . import views

urlpatterns =[
       path('ServiceList/', views.ServiceList,name="ServiceList"),
       path('createServiceWithForm/', views.createServiceWithForm,name="createServicewithForm"),
       path('deleteService/<int:id>', views.deleteService,name="deleteService"),
       path('updateService/<int:id>', views.updateService,name="updateService"),




]