from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class homepage(TemplateView):
    template_name = 'home.html'

class flightpage(TemplateView):
    template_name = 'flights.html'
    
class aboutuspage(TemplateView):
    template_name = 'aboutus.html'
    
class contactpage(TemplateView):
    template_name = 'contact.html'
    
class detailspage(TemplateView):
    template_name = 'details.html'
    
class indexpage(TemplateView):
    template_name = 'index.html'
    
class INNpage(TemplateView):
    template_name = 'inn.html'  # Corrected
    
class ToursPage(TemplateView):
    template_name = 'tours.html'
