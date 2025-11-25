from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from myFirstApp.models import Car

# Create your views here.
def myView(request):
    carList = Car.objects.all().order_by("title")
    context={
        "carList":carList
    }
    return render(request, "myFirstApp/carList.html",context)

class CarListView(TemplateView):
    template_name = "myFirstApp/carList.html"

    def getContextData(self):
        carList = Car.objects.all().order_by("title")
        return {
            "carList":carList
        }

def myTestView(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")