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
    if request.method == "POST":
        paper_form = PaperForm(request.POST or None, request.FILES)
        images = ImageForm(request.POST or None, prefix="images")
        reports = ReportForm(request.POST or None, prefix="reports")
        structure_research = StructureResearchForm(request.POST or None, prefix="structure_research")
        rfa_research = RfaResearchForm(request.POST or None, prefix="rfa_research")
        furie_research = FurieResearchForm(request.POST or None, prefix="furie_research")
        krs_research = KrsResearchForm(request.POST or None, prefix="krs_research")
        him_image = HimImageForm(request.POST or None, prefix="him_image")

    else:
        form = PaperForm()

    return render(
        request,
        "paper/createPaper.html",
        {
            "form": form,
        },
    )


def detail_view(request, pk):
    paper = get_object_or_404(Paper, id=pk)
    context = {"paper": paper}
    return render(request, "paper/detailPaper.html", context)
