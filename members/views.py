

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def people(request):
    return render(request,'people.html')