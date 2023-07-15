from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')

def details(request):
    return render(request, 'myapp/details.html')