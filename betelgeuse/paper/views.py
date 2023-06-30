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
        form = PaperForm(request.POST)
        report_formset = PaperReportFormSet(request.POST, request.FILES, prefix="reports")

        if form.is_valid() and report_formset.is_valid():
            paper = form.save()
            report_formset.instance = paper
            report_formset.save()

            return index(request)
        else:
            print(report_formset.errors)
    else:
        form = PaperForm()
        report_formset = PaperReportFormSet(prefix="reports")

    return render(request, "paper/addPaper.html", {"form": form, "report_formset": report_formset})


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
