from django import forms
from .models import *
from django.forms import inlineformset_factory


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"


PaperReportFormSet = inlineformset_factory(Paper, Report, form=ReportForm, extra=1)


class PaperForm(forms.ModelForm):
    report_formset = PaperReportFormSet(prefix="reports")

    class Meta:
        model = Paper
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"required": "required", "type": "date"}),
            "file": forms.ClearableFileInput(attrs={"required": "required"}),
        }
