from django.shortcuts import (get_object_or_404,
                              render,HttpResponse,
                              HttpResponseRedirect)

from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# relative import of forms
from .models import User
from .forms import FunsForm, UserRegisterForm,UserLoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import json


### Realizing CRUD
#TODO:Class Based Generic Views Django (Create, Retrieve, Update, Delete)

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

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
        return HttpResponseRedirect("/funs/")
 
    return render(request, "delete_view.html", context)

# Регистрация
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)


# Аутентификация (вход)
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = AuthenticationForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)