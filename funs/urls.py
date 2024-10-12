from django.urls import path
from funs.views import MyView
from . import views
from .views import register, login_view

urlpatterns = [
    
    #path("", views.index, name="index"),
    path('about/', MyView.as_view()),
    path("", views.create_view, name="create_view"),
    # TODO: realize url routing
    path("", views.list_view, name="list_view"),
    path("<id>", views.detail_view, name="detail_view"),
    path("<id>/update", views.update_view, name="update_view"),
    path('<id>/delete', views.delete_view, name="delete_view" ),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]