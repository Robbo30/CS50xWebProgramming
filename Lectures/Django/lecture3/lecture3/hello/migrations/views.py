from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def ben(request):
    return HttpResponse("Hello, Ben!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalise()
    })