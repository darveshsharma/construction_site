from django.shortcuts import render, HttpResponse
from datetime import datetime     
from myapp.models import Contact  
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'index.html') 
    #return HttpResponse("this is homepage")

def service(request):
    return render(request, 'services.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact= request.POST.get('contact')
        desc = request.POST.get('desc')
        contact1= Contact(name=name, email=email, contact=contact, desc=desc, date=datetime.today())
        contact1.save()
        messages.success(request, 'Your message has been sent ')
    return render(request, 'contact.html') 