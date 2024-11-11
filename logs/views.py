from django.shortcuts import render
from django.http import HttpResponse

def home(homereq):
    return HttpResponse("home")
