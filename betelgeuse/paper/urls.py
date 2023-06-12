from django.urls import path
from . import views

urlpatterns = [path("", views.home, name="paper-home"), path("about", views.about, name="paper-about")]
