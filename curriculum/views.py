from django.shortcuts import render
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
