from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *


def index(request):
    papers = Paper.objects.all()
    return render(request, "paper/index.html", {"papers": papers})


def addPaper(request):
    ReportFormSet = forms.formsets.formset_factory(ReportForm, extra=1)
    ImageFormSet = forms.formsets.formset_factory(ImageForm, extra=1)
    StructureResearchFormSet = forms.formsets.formset_factory(StructureResearchForm, extra=1)
    RfaResearchFormSet = forms.formsets.formset_factory(RfaResearchForm, extra=1)
    FurieResearchFormSet = forms.formsets.formset_factory(FurieResearchForm, extra=1)
    KrsResearchFormSet = forms.formsets.formset_factory(KrsResearchForm, extra=1)

    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        reports_formset = ReportFormSet(request.POST, prefix="report_form")
        images_formset = ImageFormSet(request.POST, request.FILES, prefix="image_form")
        structure_formset = StructureResearchFormSet(request.POST, request.FILES, prefix="structure_form")
        rfa_formset = RfaResearchFormSet(request.POST, request.FILES, prefix="rfa_form")
        furie_formset = FurieResearchFormSet(request.POST, request.FILES, prefix="furie_form")
        krs_formset = KrsResearchFormSet(request.POST, request.FILES, prefix="krs_form")

        if (
            form.is_valid()
            and reports_formset.is_valid()
            and images_formset.is_valid()
            and structure_formset.is_valid()
            and rfa_formset.is_valid()
            and furie_formset.is_valid()
            and krs_formset.is_valid()
        ):
            paper = form.save(commit=False)
            paper.save()

            for report_form in reports_formset:
                report = report_form.save(commit=False)
                report.paper = paper
                report.save()

            for image_form in images_formset:
                image = image_form.save(commit=False)
                image.paper = paper
                image.save()

            for structure_form in structure_formset:
                structure = structure_form.save(commit=False)
                structure.paper = paper
                structure.save()

            for rfa_form in rfa_formset:
                rfa = rfa_form.save(commit=False)
                rfa.paper = paper
                rfa.save()

            for furie_form in furie_formset:
                furie = furie_form.save(commit=False)
                furie.paper = paper
                furie.save()

            for krs_form in krs_formset:
                krs = krs_form.save(commit=False)
                krs.paper = paper
                krs.save()

            return index(request)

    else:
        form = PaperForm()
        reports_formset = ReportFormSet(prefix="report_form")
        images_formset = ImageFormSet(prefix="image_form")
        structure_formset = StructureResearchFormSet(prefix="structure_form")
        rfa_formset = RfaResearchFormSet(prefix="rfa_form")
        furie_formset = FurieResearchFormSet(prefix="furie_form")
        krs_formset = KrsResearchFormSet(prefix="krs_form")

    context = {
        "form": form,
        "reports_formset": reports_formset,
        "images_formset": images_formset,
        "structure_formset": structure_formset,
        "rfa_formset": rfa_formset,
        "furie_formset": furie_formset,
        "krs_formset": krs_formset,
    }
    return render(request, "paper/addPaper.html", context)


def about(request):
    return HttpResponse("<h1>О проекте</h1>")
