from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from datetime import date

class Home(TemplateView):
    template_name = "home.html"