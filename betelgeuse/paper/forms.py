from django import forms
from .models import *


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["date", "file"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["bw_positive", "color_positive", "date_capture"]


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
    report_formset = forms.inlineformset_factory(Paper, Report, form=ReportForm, extra=1)
    image_formset = forms.inlineformset_factory(Paper, Image, form=ImageForm, extra=1)
    structure_formset = forms.inlineformset_factory(Paper, StructureResearch, form=StructureResearchForm, extra=1)
    rfa_formset = forms.inlineformset_factory(Paper, RfaResearch, form=RfaResearchForm, extra=1)
    furie_formset = forms.inlineformset_factory(Paper, FurieResearch, form=FurieResearchForm, extra=1)
    krs_formset = forms.inlineformset_factory(Paper, KrsResearch, form=KrsResearchForm, extra=1)

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

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        self.fields["subtitles"].widget.attrs["class"] = "select2"
        self.fields["authors"].widget.attrs["class"] = "select2"

    def save(self, commit=True):
        instance = super(PaperForm, self).save(commit=commit)
        if commit:
            self.report_formset.instance = instance
            self.report_formset.save()

            self.image_formset.instance = instance
            self.image_formset.save()

            self.structure_formset.instance = instance
            self.structure_formset.save()

            self.rfa_formset.instance = instance
            self.rfa_formset.save()

            self.furie_formset.instance = instance
            self.furie_formset.save()

            self.krs_formset.instance = instance
            self.krs_formset.save()

        return instance
