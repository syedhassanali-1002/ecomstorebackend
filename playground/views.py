from django.shortcuts import render
from django.http import HttpResponse

def hello_fun(request):
    return render(request, 'hello.html', {"name": "Sunny"})