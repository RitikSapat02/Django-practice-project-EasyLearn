from django.shortcuts import render
from .models import about,slider,client

# Create your views here.
def home(request):
    about_data = about.objects.all()[0] #we want only first one
    sliders_data = slider.objects.all()
    clients_data = client.objects.all()

    context={
        'about':about_data,
        'sliders':sliders_data,
        'clients':clients_data,
    }
    # return HttpResponse("This is our Home Page")
    return render(request,'index.html',context)

def aboutus(request):
    # data ="get all data from database"
    # return HttpResponse(data)
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("This is our Contact page")
    return render(request,'contact.html')


