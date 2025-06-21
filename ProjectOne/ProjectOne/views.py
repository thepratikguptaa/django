from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello User, You are at Django Home Page')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello User, You are at Django about Page')

def contact(request):
    return HttpResponse('Hello User, You are at Django contact Page')