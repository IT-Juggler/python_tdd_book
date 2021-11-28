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
    _error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            _error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': _error})

def new_list(request):
    """docstring"""
    list_ = List.objects.create()
    item = Item(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)
