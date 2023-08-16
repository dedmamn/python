from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic

# Create your views here.

from .models import *
from .forms import *


class PaperList(generic.ListView):
    model = Paper
    context_object_name = "papers"
    template_name = "paper/index.html"
    paginate_by = 10


def create_paper(request):
    paper_form = PaperForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if paper_form.is_valid():
            paper = paper_form.save(commit=False)

            report_formset = PaperForm.report_formset(request.POST or None, request.FILES, instance=paper)
            image_formset = PaperForm.image_formset(request.POST or None, request.FILES, instance=paper)
            himImage_formset = PaperForm.himImage_formset(request.POST or None, request.FILES, instance=paper)
            structureResearch_formset = PaperForm.structure_formset(request.POST or None, request.FILES, instance=paper)
            rfaResearch_formset = PaperForm.rfa_formset(request.POST or None, request.FILES, instance=paper)
            furieResearch_formset = PaperForm.furie_formset(request.POST or None, request.FILES, instance=paper)
            krsResearch_formset = PaperForm.krs_formset(request.POST or None, request.FILES, instance=paper)

            if (
                report_formset.is_valid()
                and image_formset.is_valid()
                and himImage_formset.is_valid()
                and structureResearch_formset.is_valid()
                and rfaResearch_formset.is_valid()
                and furieResearch_formset.is_valid()
                and krsResearch_formset.is_valid()
            ):
                paper.save()

                report_formset.save()
                image_formset.save()
                himImage_formset.save()
                structureResearch_formset.save()
                rfaResearch_formset.save()
                furieResearch_formset.save()
                krsResearch_formset.save()

                return HttpResponseRedirect("/")
            else:
                pass

    return render(
        request,
        "paper/createPaper.html",
        {
            "form": paper_form,
        },
    )


def detail_view(request, pk):
    paper = get_object_or_404(Paper, id=pk)
    context = {"paper": paper}
    return render(request, "paper/detailPaper.html", context)
