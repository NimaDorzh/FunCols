from django.shortcuts import render

from django.http import HttpResponse

# relative import of forms
from .models import User
from .forms import FunsForm



### Realizing CRUD

# Create
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = FunsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)

# Simple View
def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = User.objects.all()
         
    return render(request, "list_view.html", context)

# Detailed view
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = User.objects.get(id = id)
         
    return render(request, "detail_view.html", context)