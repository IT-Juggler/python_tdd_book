"""Build views with Django"""
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.forms import ItemForm
from lists.models import Item, List

def home_page(request):
    """Render the home page."""
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    """Render the list page."""
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)

    return render(request, 'list.html', {'list': list_, "form": form})

def new_list(request):
    """docstring"""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    return render(request, 'home.html', {"form": form})
