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

            is_report_valid = (
                not any(request.POST.get(prefix, "") for prefix in report_formset.prefix) or report_formset.is_valid()
            )
            is_image_valid = (
                not any(request.POST.get(prefix, "") for prefix in image_formset.prefix) or image_formset.is_valid()
            )
            is_himImage_valid = (
                not any(request.POST.get(prefix, "") for prefix in himImage_formset.prefix)
                or himImage_formset.is_valid()
            )
            is_structureResearch_valid = (
                not any(request.POST.get(prefix, "") for prefix in structureResearch_formset.prefix)
                or structureResearch_formset.is_valid()
            )
            is_rfaResearch_valid = (
                not any(request.POST.get(prefix, "") for prefix in rfaResearch_formset.prefix)
                or rfaResearch_formset.is_valid()
            )
            is_furieResearch_valid = (
                not any(request.POST.get(prefix, "") for prefix in furieResearch_formset.prefix)
                or furieResearch_formset.is_valid()
            )
            is_krsResearch_valid = (
                not any(request.POST.get(prefix, "") for prefix in krsResearch_formset.prefix)
                or krsResearch_formset.is_valid()
            )

            if (
                is_report_valid
                and is_image_valid
                and is_himImage_valid
                and is_structureResearch_valid
                and is_rfaResearch_valid
                and is_furieResearch_valid
                and is_krsResearch_valid
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
                print(report_formset.errors)
                print(image_formset.errors)
                print(himImage_formset.errors)
                print(structureResearch_formset.errors)
                print(rfaResearch_formset.errors)
                print(furieResearch_formset.errors)
                print(krsResearch_formset.errors)

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
