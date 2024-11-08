from django.shortcuts import render
from django.urls import path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Population, Location, Factor, Threat
from .forms import PopulationForm, LocationForm, FactorForm, ThreatForm
# Create your views here.

@login_required(login_url='login')
def population_list(request):
    populations = Population.objects.all()
    return render(request, 'population_list.html', {'populations': populations})




@login_required(login_url='login')
def population_detail(request, pk):
    population = get_object_or_404(Population, pk=pk)
    return render(request, 'population_detail.html', {'population': population})


@login_required(login_url='login')
def population_create(request):
    if request.method == "POST":
        form = PopulationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('population_list')
    else:
        form = PopulationForm()
    return render(request, 'population_form.html', {'form': form})




@login_required(login_url='login')
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})

@login_required(login_url='login')
def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'location_detail.html', {'location': location})

@login_required(login_url='login')
def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'location_form.html', {'form': form})



@login_required
def index(request):
    return render(request, 'index.html')