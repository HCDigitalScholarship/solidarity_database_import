from django.shortcuts import render
from data.models import *

# Create your views here.
def index(request):
        return render(request, 'index.html')

def data(request):
    data = Data.object.all()
    return render(request, 'data.html', {'data':data})
