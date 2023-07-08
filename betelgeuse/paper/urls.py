from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaperList.as_view(), name="paper-home"),
    # path("create", views.PaperCreate.as_view(), name="paper_create"),
    path("<int:pk>", views.PaperUpdate.as_view(), name="paper-update"),
    # path("<int:pk>", views.updatePaper, name="paper-update"),
    path("addPaper", views.PaperCreate.as_view(), name="paper-add"),
]
