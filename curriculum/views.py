from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def index(request):
    projects = Projects.objects.all()
    context = {"projects":projects}

    return render(request,'index.html',context)

def project(request, id):
    project = Projects.objects.get(id=id)
    context = {"project":project}

    return render(request,'project.html',context)

def picture(request, id):
    project = Projects.objects.get(id=id)
    context = {"project":project}

    return render(request,'foto.html',context)

def contacto(request):
    if request.method == 'POST':
        Contacto.objects.create(Name=request.POST['name'],email=request.POST['email'],title=request.POST['subject'],message=request.POST['message'])

    return redirect('/')
