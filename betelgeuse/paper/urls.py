from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="paper-home"),
    path("about", views.about, name="paper-about"),
    path("addPaper", views.addPaper, name="paper-add"),
]
