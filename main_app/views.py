from django.shortcuts import render
finchcollector = [
  {'name': 'Lolo', 'breed': 'goldfinch', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'parrot crossbukk', 'description': 'talkative', 'age': 2},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')