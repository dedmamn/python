from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *


def index(request):
    papers = Paper.objects.all()
    return render(request, "paper/index.html", {"papers": papers})


def addPaper(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddPaperForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = AddPaperForm()
        return render(request, "paper/addPaper.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPaperForm()
    return render(request, "paper/addPaper.html", {"title": "Добавление записи", "form": form})


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
