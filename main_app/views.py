import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.toys.all().values_list('id')
    # instantiate feeding form to be rendered
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


    #__all__ tells django to render all fields for the input i.e. name, breed, description, age - its like a shortcut 


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age'] #order matters


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finch'


def add_feeding(request, finch_id):
    #create a model form instance using the data that was submitted in the form
    form = FeedingForm(request.POST)
    #must validate the form
    if form.is_valid():
        #we want a model instance but cant save it to the db yet cos we havent assigned cat_id FK
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id) 

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'


  #associating a toy with a finch
def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def cancel_assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)


