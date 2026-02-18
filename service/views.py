from django.shortcuts import render,HttpResponse,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.

def ServiceList(request):

    Services = Service.object.all().values()
    print(ServiceList)
    return render(request,'Service/ServiceList.html',{"Services":Service})

def createServiceWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        return HttpResponse("SERVICE CREATED")
    else:
        #form object create --> html
        form = ServiceForm(request.POST)
        return render(request,"Service/createService.html",{"form":form})

def deleteService(request):
    print("id from url= ",id)
    Service(id=id).delete()
    return redirect(ServiceList)



def updateService(request):
    #database existing user... id -->
    service =Service.get(id=id) #select * from employee where id = 1

    if request.method == "POST":
        form = ServiceForm(request.POST,instance=service)
        form.save()
        return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)
        return render(request,"Service/UpdateService.html",{"form":form})