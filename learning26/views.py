from  django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"AboutUs.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def movies(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")

def recap(request):
    return render(request,"recap.html")

def recipe(request):
    ingredient = ["noodles","water"]
    data={"name":"maggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def team(request):
    playerlist = ["Rahul","Virat","Gill","Hardik"]
    data={"Name":"TEAM INDIA","captain":"Rohit Sharma","players":playerlist,"trophies":2}
    return render(request,"team.html",data)

def person(request):
    PersonName = ["A","B","C","D","E"]
    data={"NameOfPerson":PersonName,"age":15}
    return render(request,"person.html",data)