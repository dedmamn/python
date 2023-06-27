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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # obj = Paper()
            # obj.code = form.cleaned_data["code"]
            # obj.title = form.cleaned_data["title"]
            # obj.year_start = form.cleaned_data["year_start"]
            # obj.year_end = form.cleaned_data["year_end"]
            # obj.url = form.cleaned_data["url"]
            # obj.subtitles = form.cleaned_data["subtitles"]
            # obj.images = form.cleaned_data["images"]
            # obj.authors = form.cleaned_data["authors"]
            # obj.additional = form.cleaned_data["additional"]
            # obj.himinfo = form.cleaned_data["himinfo"]
            # obj.save()

            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPaperForm()
    return render(request, "paper/addPaper.html", {"title": "Добавление записи", "form": form})


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
