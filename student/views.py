

# Create your views here.
from django.shortcuts import render



def Home(request):
    return render(request,"Home.html")

def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)    
    #student/studentDashboard.html
    #folder/filenam

def studentMarks(request):
    marks = {"maths":75,"science":84,"english":80}
    return render(request,"student/studentMarks.html",marks)