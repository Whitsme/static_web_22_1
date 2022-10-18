"""
   Aaron Whitaker
CIS218 - Web Application Programming
9/22/2022 
"""

from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

# points to the template for each page
class HomePageView(TemplateView):
    template_name = "home.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class ProjectsPageView(TemplateView):
    template_name = "projects.html"
