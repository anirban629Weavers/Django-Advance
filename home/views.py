from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    peoples=[
        {"name": "Tiler","age": 49}, 
        {"name": "Garwin","age": 100}, 
        {"name": "Minda","age": 84}, 
        {"name": "Mattie","age": 44}, 
        {"name": "Rachael","age": 63}, 
        {"name": "Doralynn","age": 24}, 
        {"name": "Ashia","age": 19}, 
        {"name": "Orsola","age": 47},
        {"name": "Orsola","age": 14},
        ]
    return render(request, 'home/index.html',context={'peoples':peoples})

def about(request):
    return render(request, 'home/about.html',context={'title': 'About'})


def contact(request):
    return render(request, 'home/contact.html',context={'title': 'Contact'})
