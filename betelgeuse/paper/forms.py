from django import forms
from .models import *


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


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

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        self.fields["authors"].widget.attrs["class"] = "select2"

    def save(self, commit=True):
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

        return instance
