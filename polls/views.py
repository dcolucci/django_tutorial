from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(type(args))
    return HttpResponse("it works b")
