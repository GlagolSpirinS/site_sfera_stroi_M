from django.shortcuts import render, get_object_or_404
from .models import ObjectMain, Managers, Jobs, Object

def home(request):
    objects = ObjectMain.objects.all()
    return render(request, 'index.html', {'objects': objects})
def personal(request):
    objects = Managers.objects.all()
    return render(request, 'personal.html', {'objects': objects})

def job(request):
    objects = Jobs.objects.all()
    return render(request, 'job.html', {'objects': objects})
def place(request):
    objects = Object.objects.all()
    return render(request, "place.html", {'objects': objects})
def partner(request):
    return render(request, 'partner.html')
def contact(request):
    return render(request, 'contact.html')
def job_detail(request, id):
    objects = get_object_or_404(Jobs, id=id)
    return render(request, 'job_detail.html', {'job': objects})
