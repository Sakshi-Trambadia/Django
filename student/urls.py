from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.Home),
   path("dashboard/",views.studentDashboard),
   path("marks/",views.studentMarks)
]