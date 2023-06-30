from django import forms
from .models import Paper, Report, Image, StructureResearch, RfaResearch, FurieResearch, KrsResearch


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["date", "file"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["bw_positive", "color_positive"]


class StructureResearchForm(forms.ModelForm):
    class Meta:
        model = StructureResearch
        fields = ["hertzberg", "graf_c", "discription"]


class RfaResearchForm(forms.ModelForm):
    class Meta:
        model = RfaResearch
        fields = ["image", "txt", "parameters", "result"]


class FurieResearchForm(forms.ModelForm):
    class Meta:
        model = FurieResearch
        fields = ["image", "txt", "parameters", "result"]


class KrsResearchForm(forms.ModelForm):
    class Meta:
        model = KrsResearch
        fields = ["image", "txt", "parameters", "result"]


class PaperForm(forms.ModelForm):
    reports = forms.formsets.BaseFormSet(form=ReportForm, prefix="report_form")
    images = forms.formsets.BaseFormSet(form=ImageForm, prefix="image_form")
    structure_researches = forms.formsets.BaseFormSet(form=StructureResearchForm, prefix="structure_form")
    rfa_researches = forms.formsets.BaseFormSet(form=RfaResearchForm, prefix="rfa_form")
    furie_researches = forms.formsets.BaseFormSet(form=FurieResearchForm, prefix="furie_form")
    krs_researches = forms.formsets.BaseFormSet(form=KrsResearchForm, prefix="krs_form")

    class Meta:
        model = Paper
        fields = [
            "code",
            "title",
            "year_start",
            "year_end",
            "url",
            "subtitles",
            "authors",
            "year_restoration",
            "passepartout",
            "thickness",
            "ph",
            "HimImage",
        ]
