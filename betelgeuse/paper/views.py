from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *


def index(request):
    papers = Paper.objects.all()
    return render(request, "paper/index.html", {"papers": papers})


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
