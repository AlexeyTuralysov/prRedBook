from django import forms
from .models import Population, Location, Factor, Threat


class PopulationForm(forms.ModelForm):
    class Meta:
        model = Population
        fields = ['name', 'description', 'date', 'time', 'total_count', 'male_count', 'female_count', 'location']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'date', 'time', 'latitude', 'longitude']

class FactorForm(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['location', 'type', 'name', 'description', 'level', 'status', 'date', 'time']

class ThreatForm(forms.ModelForm):
    class Meta:
        model = Threat
        fields = ['location', 'name', 'description', 'date', 'time']