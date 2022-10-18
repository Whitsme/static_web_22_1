"""
   Aaron Whitaker
CIS218 - Web Application Programming
9/22/2022 
"""

from django.urls import path


from .views import HomePageView, ContactPageView, ProjectsPageView

# points to the correct page by page name
urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
]

