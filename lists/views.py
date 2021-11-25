"""Build views with Django"""
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    """Render the home page."""
    return render(request, 'home.html')

def view_list(request):
    """Render the list page."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """docstring"""
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
