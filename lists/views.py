"""Build views with Django"""
from django.shortcuts import render

def home_page(request):
    """Render the home page."""
    return render(request, 'home.html')
