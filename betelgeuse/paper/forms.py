from django import forms
from .models import *
from django_selectize import forms as s2forms
from formset.widgets import DateInput, Selectize, UploadedFileInput, SelectizeMultiple
from django.views.generic.edit import FormView


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={"class": "reports__date--input", "type": "date", "id": "date", "name": "date"}
            ),
            "file": forms.FileInput(
                attrs={"class": "reports__file--input", "type": "file", "id": "report", "name": "report"}
            ),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        widgets = {
            "color_positive": forms.FileInput(
                attrs={
                    "class": "images__color-positive--input",
                    "id": "color-positive",
                    "onchange": "document.getElementById('output_color-positive').src = window.URL.createObjectURL(this.files[0])",
                }
            ),
            "bw_positive": forms.FileInput(
                attrs={
                    "class": "images__bw-positive--input",
                    "id": "bw-positive",
                    "onchange": "document.getElementById('output_bw-positive').src = window.URL.createObjectURL(this.files[0])",
                }
            ),
            "date_capture": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"class": "images__capture-date--input", "id": "Capture-date", "type": "date"},
            ),
        }


class StructureResearchForm(forms.ModelForm):
    class Meta:
        model = StructureResearch
        fields = "__all__"


class RfaResearchForm(forms.ModelForm):
    class Meta:
        model = RfaResearch
        fields = "__all__"


class FurieResearchForm(forms.ModelForm):
    class Meta:
        model = FurieResearch
        fields = "__all__"


class KrsResearchForm(forms.ModelForm):
    class Meta:
        model = KrsResearch
        fields = "__all__"


class HimImageForm(forms.ModelForm):
    class Meta:
        model = HimImage
        fields = "__all__"
        widgets = {
            "microscopy": UploadedFileInput,
            "uf": UploadedFileInput,
            "express_test": UploadedFileInput,
        }


# class AuthorForm(forms.Widget):
#     name = forms.models.ModelChoiceField(
#         label="Авторы",
#         queryset=Author.objects.all(),
#         widget=SelectizeMultiple(search_lookup="name__icontains"),
#     )


class PaperForm(forms.ModelForm):
    report_formset = forms.inlineformset_factory(Paper, Report, form=ReportForm, extra=1, can_delete_extra=False)
    image_formset = forms.inlineformset_factory(Paper, Image, form=ImageForm, extra=1, can_delete_extra=False)
    structure_formset = forms.inlineformset_factory(
        Paper, StructureResearch, form=StructureResearchForm, extra=1, can_delete_extra=False
    )
    rfa_formset = forms.inlineformset_factory(Paper, RfaResearch, form=RfaResearchForm, extra=1, can_delete_extra=False)
    furie_formset = forms.inlineformset_factory(
        Paper, FurieResearch, form=FurieResearchForm, extra=1, can_delete_extra=False
    )
    krs_formset = forms.inlineformset_factory(Paper, KrsResearch, form=KrsResearchForm, extra=1, can_delete_extra=False)
    himImage_formset = forms.inlineformset_factory(Paper, HimImage, form=HimImageForm, extra=1, can_delete_extra=False)

    class Meta:
        model = Paper
        fields = "__all__"
        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "create-paper__element--input create-paper__code--input",
                    "type": "text",
                    "id": "code",
                    "name": "code",
                    "required": True,
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "create-paper__element--input create-paper__title--input",
                    "type": "text",
                    "id": "title",
                    "name": "title",
                    "required": True,
                }
            ),
            "subtitle": forms.TextInput(
                attrs={
                    "class": "create-paper__element--input create-paper__subtitle--input",
                    "type": "text",
                    "id": "subtitle",
                    "name": "subtitle",
                    # "required": True,
                }
            ),
            "authors": forms.SelectMultiple(
                attrs={
                    "class": "create-paper__element--input create-paper__authors--input",
                    "id": "authors",
                    "name": "authors",
                }
            ),
            "year_start": forms.NumberInput(
                attrs={
                    "class": "create-paper__element--input create-paper__year-start--input",
                    "type": "number",
                    "id": "year-start",
                    "name": "year-start",
                    "min": "0",
                    "max": "9999",
                    "required": True,
                }
            ),
            "year_end": forms.NumberInput(
                attrs={
                    "class": "create-paper__element--input create-paper__year-end--input",
                    "type": "number",
                    "id": "year-end",
                    "name": "year-end",
                    "min": "0",
                    "max": "9999",
                    # "required": True,
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "create-paper__element--input create-paper__url--input",
                    "type": "text",
                    "id": "url",
                    "name": "url",
                    "required": True,
                }
            ),
            "year_restoration": forms.NumberInput(
                attrs={
                    "class": "create-paper__element--input create-paper__year-restoration--input",
                    "type": "number",
                    "id": "year-restoration",
                    "name": "year-restoration",
                    "min": "0",
                    "max": "9999",
                    # "required": True,
                }
            ),
            "passepartout": forms.CheckboxInput(
                attrs={
                    "class": "create-paper__element--input create-paper__passepartout--input",
                    "type": "checkbox",
                    "id": "passepartout",
                    "name": "passepartout",
                    # "required": True,
                }
            ),
            "thickness": forms.NumberInput(
                attrs={
                    "class": "create-paper__element--input create-paper__thickness--input",
                    "type": "number",
                    "id": "thickness",
                    "name": "thickness",
                    "min": "0",
                    "max": "9999",
                    # "required": True,
                }
            ),
            "ph": forms.NumberInput(
                attrs={
                    "class": "create-paper__element--input create-paper__ph--input",
                    "type": "number",
                    "id": "ph",
                    "name": "ph",
                    "min": "0",
                    "max": "14",
                    # "required": True,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)

    def save(self, commit=False):
        instance = super(PaperForm, self).save(commit=commit)
        if commit:
            self.himImage_formset.instance = instance
            self.himImage_formset.save()

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

            instance.save()

        return instance
