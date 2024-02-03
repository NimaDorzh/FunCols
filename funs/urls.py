from django.urls import path

from . import views

urlpatterns = [
    
    #path("", views.index, name="index"),
    path("", views.create_view, name="create_view"),

    # TODO: realize url routing
    path("", views.list_view, name="list_view"),
    
]