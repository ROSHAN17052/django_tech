from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Service(request):
    return render(request,'service.html')

def Blog(request):
    return render(request,'blog.html')


def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')