from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Register your models here.

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def shopping(request):
    return HttpResponse("Welcome to shopping")