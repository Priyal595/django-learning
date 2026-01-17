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
    
    text = "Lorem ipsum Morbi erat ex, lacinia nec efficitur eget, sagittis ut orci. Etiam in dolor placerat, pharetra ligula et, bibendum neque. Vestibulum vitae congue lectus, sed ultricies augue. Nam iaculis elit nec velit luctus, vitae rutrum nunc imperdiet. Nunc vel turpis sit amet lectus pellentesque tincidunt. Proin commodo tincidunt enim, at sodales mi dictum ac. Maecenas molestie, metus quis malesuada dictum, leo erat egestas lacus, sit amet tristique urna magna a diam. Donec ultricies dui sit amet mi ornare egestas. Phasellus ultricies lectus non interdum pellentesque. Cras nisi tellus, feugiat sed enim quis, tristique interdum lacus. Sed vel pharetra arcu, ac fermentum neque. Morbi mollis sollicitudin varius. Ut sit amet vulputate velit."
    return  render(request, 'index.html', context={'peoples': peoples, 'text': text})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def success_page(request):
    return HttpResponse("<h1> this is a success page </h1>")