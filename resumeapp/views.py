from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .forms import *
from .models import *


# Create your views here.
def index(request):
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
    about = AboutModel.objects.all()
    resume = ResumeModel.objects.all()
    skil = SkilModel.objects.all()
    servis = ServisModel.objects.all()

    ctx = {
        'form': form,
        'about': about,
        'resume1': resume[:3],
        'resume2': resume[3:6],
        'servis': servis,
        'skil': skil,
    }
    return render(request, 'index.html', ctx)
