from django.shortcuts import render
from django.http import HttpResponse
def homepage(request):
    return render(request, 'header/homepage.html')

def about(request):
    return render(request, 'header/about.html')
    
def contact(request):
    return render(request, 'header/contact.html')
def downloading(request):
    return render(request, 'header/down.html')