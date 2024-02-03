from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


# Read Detailed view
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = User.objects.get(id = id)
         
    return render(request, "detail_view.html", context)


#TODO: Figure out ListView
# Read Simple View
def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = User.objects.all()
         
    return render(request, "list_view.html", context)

# Update View
def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, id = id)
 
    # pass the object as instance in form
    form = FunsForm(request.POST, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)


# Delete View
def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)