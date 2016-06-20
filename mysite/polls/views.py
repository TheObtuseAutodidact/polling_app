# from django.shortcuts import render  ### this was a default import

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
