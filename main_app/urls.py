#this is where we will define all paths for finchcollector app ,


#! to define routes we need to import a path function and our views file:
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
]