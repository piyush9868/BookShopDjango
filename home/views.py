from django.shortcuts import render, HttpResponse
from datetime import date
from home.models import Contact

# Create your views here.

def index(request):
    context = {
        "password" : "x@22Ps",
        "username" : "piyush9868"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        dte = date.today()
        contact = Contact(name = name, email=email,phone=phone, desc=desc, date=dte)
        contact.save()
    return render(request, 'contact.html')