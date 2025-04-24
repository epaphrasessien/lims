from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Register your models here.

# Create your views here.
from .models import *


def home(request):
    return render(request,"home.html",context={"current_tab": "home"})

def students(request):
    return render(request,"students.html",context={"current_tab": "students"})


def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})

def students_tab(request):
    students = student.objects.all()
    return render(request,"students.html",
                  content={"current_tab": "students",
                          "students":students})