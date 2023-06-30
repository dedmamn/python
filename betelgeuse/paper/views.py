from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *


def index(request):
    papers = Paper.objects.all()
    return render(request, "paper/index.html", {"papers": papers})


def addPaper(request):
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = PaperForm()

    return render(request, "paper/addPaper.html", {"paper_form": form})


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
