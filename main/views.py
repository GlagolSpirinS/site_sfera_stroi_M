from django.shortcuts import render, get_object_or_404, redirect
from .models import ObjectMain, Managers, Jobs, Object, Partner
from .forms import ApplicantForm


def home(request):
    main_objects = ObjectMain.objects.all()
    return render(request, 'index.html', {'objects': main_objects})


def company(request):
    company_objects = ObjectMain.objects.all()
    return render(request, 'company.html', {'objects': company_objects})


def personal(request):
    managers = Managers.objects.all()
    return render(request, 'personal.html', {'objects': managers})


def job(request):
    job_list = Jobs.objects.all()
    return render(request, 'job.html', {'objects': job_list})


def place(request):
    places = Object.objects.all()
    return render(request, "place.html", {'objects': places})


def partner(request):
    partners = Partner.objects.all()
    return render(request, 'partner.html', {"objects": partners})


def contact(request):
    return render(request, 'contact.html')


def job_detail(request, id):
    job = get_object_or_404(Jobs, id=id)
    return render(request, 'job_detail.html', {'job': job})


def object_detail(request, id):
    obj = get_object_or_404(Object, id=id)
    return render(request, 'object_detail.html', {'obj': obj})


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def object_list(request):
    is_ready = request.GET.get('is_ready')
    if is_ready is not None:
        objects = Object.objects.filter(is_ready=is_ready)
    else:
        objects = Object.objects.all()
    return render(request, 'place.html', {'objects': objects})


def apply_for_job(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job_name = job.name  # Сохраняем название профессии
            applicant.save()
            return redirect('job_detail', id=job_id)  # Перенаправляем на страницу вакансии
    else:
        form = ApplicantForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})
