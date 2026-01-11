from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return  HttpResponse("<h1>Hi this is the home page</h1>")

def success_page(request):
    return HttpResponse("<h1> this is a success page </h1>")