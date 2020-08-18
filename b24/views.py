from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request):
    #print(request.headers)
    return HttpResponse("Hello, world. You're at the polls index.")
