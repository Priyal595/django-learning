from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [
        {'name' : 'Priyal', 'age': 20},
        {'name' : 'Priyanshi', 'age': 19},
        {'name' : 'Ishan', 'age': 16},
        {'name' : 'Raghav', 'age': 21},
        {'name' : 'Sudha', 'age': 48},
    ]
    return  render(request, 'index.html', context={'peoples': peoples})


def success_page(request):
    return HttpResponse("<h1> this is a success page </h1>")