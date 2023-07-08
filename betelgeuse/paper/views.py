from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic

# Create your views here.

from .models import *
from .forms import *


class PaperList(generic.ListView):
    model = Paper
    template_name = "paper/index.html"
    context_object_name = "papers"


class PaperCreate(generic.CreateView):
    model = Paper
    template_name = "paper/addPaper.html"
    form_class = PaperForm


class PaperUpdate(generic.UpdateView):
    model = Paper
    template_name = "paper/addPaper.html"
    form_class = PaperForm


def index(request):
    papers = Paper.objects.all()
    return render(request, "paper/index.html", {"papers": papers})


def detail(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    form = PaperForm(instance=paper)
    return render(request, "paper/addPaper.html", {"paper_from": form})


def updatePaper(request, pk):
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        paper = Paper.objects.get(pk=pk)
        form = PaperForm(instance=paper)

    return render(request, "paper/addPaper.html", {"paper_form": form})


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
