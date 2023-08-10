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


class PaperCreate(generic.CreateView):
    model = Paper
    template_name = "paper/addPaper.html"
    form_class = PaperForm
    success_url = "/"


class PaperUpdate(generic.UpdateView):
    model = Paper
    template_name = "paper/addPaper.html"
    form_class = PaperForm


def create_paper(request):
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Перенаправление на нужную страницу после успешного сохранения
            return HttpResponseRedirect("/")
    else:
        form = PaperForm()

    return render(request, "paper/detailPaper.html", {"form": form})

    # def detail_view(request):
    #     # Assuming you have a primary key for the Paper object you want to display
    #     paper_id = 1

    #     paper_instance = Paper.objects.get(pk=paper_id)

    #     # Assuming you have a queryset to get all related research objects for the Paper instance
    #     reports = paper_instance.report_set.all()
    #     images = paper_instance.image_set.all()
    #     # ... and so on for other related research objects

    #     context = {
    #         "paper_instance": paper_instance,
    #         "reports": reports,
    #         "images": images,
    #         # ... and other related research objects
    #     }

    return render(request, "paper/detailPaper.html", context)


# def index(request):
#     papers = Paper.objects.all()
#     return render(request, "paper/index.html", {"papers": papers})


# def detail(request, paper_id):
#     paper = get_object_or_404(Paper, id=paper_id)
#     # paper = Paper.objects.get(pk=paper_id)
#     form = PaperForm(instance=paper)
#     return render(request, "paper/addPaper.html", {"paper_from": form})


# def updatePaper(request, pk):
#     if request.method == "POST":
#         form = PaperForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return index(request)
#     else:
#         paper = Paper.objects.get(pk=pk)
#         form = PaperForm(instance=paper)

#     return render(request, "paper/addPaper.html", {"paper_form": form})


# def addPaper(request):
#     if request.method == "POST":
#         form = PaperForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return index(request)
#     else:
#         form = PaperForm()

#     return render(request, "paper/addPaper.html", {"paper_form": form})


# def about(request):
#     return HttpResponse("<h1>О проекте</h1>")
