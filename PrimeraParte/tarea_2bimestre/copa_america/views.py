
from django.shortcuts import render
from .models import CopaAmerica

def copa_america(request):
    copas_america = CopaAmerica.objects.all()
    return render(request, 'copa_america.html', {'copas_america': copas_america})
