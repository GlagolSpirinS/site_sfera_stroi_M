from django.shortcuts import render
from .models import ObjectMain

def home(request):
    objects = ObjectMain.objects.all()
    return render(request, 'index.html', {'objects': objects})
def personal(request):
    return render(request, 'personal.html')
def job(request):
    return render(request, 'job.html')
def place(request):
    return render(request, "place.html")
def partner(request):
    return render(request, 'partner.html')
def contact(request):
    return render(request, 'contact.html')
