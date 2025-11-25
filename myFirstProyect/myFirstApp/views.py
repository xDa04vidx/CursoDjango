from django.shortcuts import render

# Create your views here.
def myView(request):
    carList =[
        {"title":"BMW"},
        {"title":"Mazda"}
    ]
    context={
        "carList":carList
    }
    return render(request, "myFirstApp/carList.html",context)