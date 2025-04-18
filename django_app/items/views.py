import requests
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.http import HttpResponse



def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/add_item.html', {'form': form})

# 🆕 New view to fetch data from Flask
def get_flask_message(request):
    try:
        response = requests.get("http://flask:5000/")
        message = response.text
    except requests.exceptions.RequestException as e:
        message = "Flask service unavailable: {e}"
    return render(request, 'items/flask_message.html', {'message': message})

def home(request):
    return HttpResponse("Hello from Django!")