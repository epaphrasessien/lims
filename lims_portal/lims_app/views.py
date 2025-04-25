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

def readers_tab(request):
    if request.method=="GET":
        readers = reader.objects.all()
        return render(request,"readers.html",
                    context={"current_tab": "readers",
                            "readers":readers}
                    )
    elif request.method=="POST":
        query = request.POST.get('query', '')
        readers = reader.objects.filter(reader_name__icontains=query)
        return render(request,"readers.html",
                    context={"current_tab": "readers",
                            "readers":readers,"query": query}
                    )

def save_reader(request):
    reader_item = reader(reference_id=request.POST['reader_ref_id'],
                           reader_name=request.POST['reader_name'],
                           reader_contact=request.POST['reader_contact'],
                           reader_course=request.POST['course'],
                           active=True
                           )
    reader_item.save()
    return redirect('/readers')