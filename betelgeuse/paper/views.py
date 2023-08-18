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

    formset_names = ["report", "image", "himImage", "structure", "rfa", "furie", "krs"]

    formsets = {
        name: getattr(PaperForm, f"{name}_formset")(request.POST or None, request.FILES, instance=paper_form.instance)
        for name in formset_names
    }

    if request.method == "POST":
        if paper_form.is_valid():
            paper = paper_form.save()

            all_valid = True
            for name, formset in formsets.items():
                is_valid = not any(request.POST.get(prefix, "") for prefix in formset.prefix) or formset.is_valid()
                if is_valid:
                    if formset.is_valid():
                        formset.save()
                    else:
                        print(formset.errors)
                        all_valid = False

            if all_valid:
                return HttpResponseRedirect("/")
            else:
                for formset in formsets.values():
                    print(formset.errors)

    return render(
        request,
        "paper/createPaper.html",
        {
            "form": paper_form,
        },
    )


def updatePaper(request, pk):
    paper = Paper.objects.get(id=pk)
    form = PaperForm(request.POST or None, instance=paper)
    images = Image.objects.filter(paper=paper)
    context = {"form": form, "images": images}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "paper/createPaper.html", context)
