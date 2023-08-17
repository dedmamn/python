from django import forms
from .models import *
from django_selectize import forms as s2forms
from django.views.generic.edit import FormView
from image_uploader_widget.widgets import ImageUploaderWidget


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(
                attrs={
                    "class": "reports__date--input",
                    "type": "date",
                    "id": "date",
                    "name": "date",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "reports__file--input",
                    "type": "file",
                    "id": "report",
                    "name": "report",
                }
            ),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        widgets = {
            "color_positive": ImageUploaderWidget(
                attrs={
                    "class": "images__color-positive--input",
                    "id": "color-positive",
                    "name": "color-positive",
                }
            ),
            "bw_positive": ImageUploaderWidget(
                attrs={
                    "class": "images__bw-positive--input",
                    "id": "bw-positive",
                    "name": "bw-positive",
                }
            ),
            "date_capture": forms.DateTimeInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "images__capture-date--input",
                    "id": "Capture-date",
                    "type": "date",
                    "name": "Capture-date",
                },
            ),
        }


class StructureResearchForm(forms.ModelForm):
    class Meta:
        model = StructureResearch
        fields = "__all__"
        widgets = {
            "hertzberg": ImageUploaderWidget(
                attrs={
                    "class": "structure__hertzberg--input",
                    "id": "hertzberg",
                    "name": "hertzberg",
                }
            ),
            "graf_c": ImageUploaderWidget(
                attrs={
                    "class": "structure__graf-c--input",
                    "id": "graf-c",
                    "name": "graf-c",
                }
            ),
            "discription": forms.SelectMultiple(
                attrs={
                    "class": "structure__discription--input",
                    "id": "discription",
                    "name": "discription",
                }
            ),
        }


class RfaResearchForm(forms.ModelForm):
    class Meta:
        model = RfaResearch
        fields = "__all__"
        widgets = {
            "image": ImageUploaderWidget(
                attrs={
                    "class": "rfa__image--input",
                    "id": "RFA-image",
                    "name": "RFA-image",
                }
            ),
            "txt": forms.FileInput(
                attrs={
                    "class": "rfa__text--input",
                    "id": "RFA-txt",
                    "name": "RFA-txt",
                }
            ),
            "parameters": forms.Textarea(
                attrs={
                    "class": "rfa__parameters--input",
                    "id": "RFA-parameters",
                    "name": "RFA-parameters",
                }
            ),
            "result": forms.Textarea(
                attrs={
                    "class": "rfa__result--input",
                    "id": "RFA-result",
                    "name": "RFA-result",
                }
            ),
        }


class FurieResearchForm(forms.ModelForm):
    class Meta:
        model = FurieResearch
        fields = "__all__"
        widgets = {
            "image": ImageUploaderWidget(
                attrs={
                    "class": "furie__image--input",
                    "id": "Furie-image",
                    "name": "Furie-image",
                }
            ),
            "txt": forms.FileInput(
                attrs={
                    "class": "furie__text--input",
                    "id": "Furie-txt",
                    "name": "Furie-txt",
                }
            ),
            "parameters": forms.Textarea(
                attrs={
                    "class": "furie__parameters--input",
                    "id": "Furie-parameters",
                    "name": "Furie-parameters",
                }
            ),
            "result": forms.Textarea(
                attrs={
                    "class": "furie__result--input",
                    "id": "Furie-result",
                    "name": "Furie-result",
                }
            ),
        }


class KrsResearchForm(forms.ModelForm):
    class Meta:
        model = KrsResearch
        fields = "__all__"
        widgets = {
            "image": ImageUploaderWidget(
                attrs={
                    "class": "krs__image--input",
                    "id": "KRS-image",
                    "name": "KRS-image",
                }
            ),
            "txt": forms.FileInput(
                attrs={
                    "class": "krs__txt--input",
                    "id": "KRS-txt",
                    "name": "KRS-txt",
                }
            ),
            "parameters": forms.Textarea(
                attrs={
                    "class": "krs__parameters--input",
                    "id": "KRS-parameters",
                    "name": "KRS-parameters",
                }
            ),
            "result": forms.Textarea(
                attrs={
                    "class": "krs__result--input",
                    "id": "KRS-result",
                    "name": "KRS-result",
                }
            ),
        }


class HimImageForm(forms.ModelForm):
    class Meta:
        model = HimImage
        fields = "__all__"
        widgets = {
            "microscopy": ImageUploaderWidget(
                attrs={
                    "class": "chem-images__microscopy--input",
                    "id": "microscopy",
                    "name": "microscopy",
                }
            ),
            "uf": ImageUploaderWidget(
                attrs={
                    "class": "chem-images__uf--input",
                    "id": "uf",
                    "name": "uf",
                }
            ),
            "express_test": ImageUploaderWidget(
                attrs={
                    "class": "chem-images__express--input",
                    "id": "ExpressTest",
                    "name": "ExpressTest",
                }
            ),
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
                }
            ),
            "authors": forms.SelectMultiple(
                attrs={
                    "class": "create-paper__element--input create-paper__authors--input",
                    "id": "authors",
                    "name": "authors",
                },
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
                }
            ),
            "passepartout": forms.CheckboxInput(
                attrs={
                    "class": "create-paper__element--input create-paper__passepartout--input",
                    "type": "checkbox",
                    "id": "passepartout",
                    "name": "passepartout",
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
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
