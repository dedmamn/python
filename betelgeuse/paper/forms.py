from django import forms
from .models import (
    Paper,
    Report,
    Image,
    StructureResearch,
    RfaResearch,
    FurieResearch,
    KrsResearch,
    Subtitle,
    Author,
    Material,
    HimImage,
)


class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ["name"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]


class HimImageForm(forms.ModelForm):
    class Meta:
        model = HimImage
        fields = ["microscopy", "uf", "express_test"]


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["name"]


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


SubtitleFormset = forms.modelformset_factory(Subtitle, form=SubtitleForm, extra=1)
AuthorFormset = forms.modelformset_factory(Author, form=AuthorForm, extra=1)
DescriptionFormset = forms.modelformset_factory(Material, form=DescriptionForm, extra=1)
ReportFormset = forms.modelformset_factory(Report, form=ReportForm, extra=1)
ImageFormset = forms.modelformset_factory(Image, form=ImageForm, extra=1)
StructureResearchFormset = forms.modelformset_factory(StructureResearch, form=StructureResearchForm, extra=1)
RfaResearchFormset = forms.modelformset_factory(RfaResearch, form=RfaResearchForm, extra=1)
FurieResearchFormset = forms.modelformset_factory(FurieResearch, form=FurieResearchForm, extra=1)
KrsResearchFormset = forms.modelformset_factory(KrsResearch, form=KrsResearchForm, extra=1)


class PaperForm(forms.ModelForm):
    subtitles = forms.ModelMultipleChoiceField(
        queryset=Subtitle.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    him_image_form = HimImageForm(prefix="him_image")

    class Meta:
        model = Paper
        fields = [
            "code",
            "title",
            "year_start",
            "year_end",
            "url",
            "year_restoration",
            "passepartout",
            "thickness",
            "ph",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "instance" in kwargs:
            self.fields["subtitles"].initial = kwargs["instance"].subtitles.all()
            self.fields["authors"].initial = kwargs["instance"].authors.all()

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            instance.subtitles.set(self.cleaned_data["subtitles"])
            instance.authors.set(self.cleaned_data["authors"])

            if self.him_image_form.is_valid():
                him_image = self.him_image_form.save()
                instance.HimImage = him_image
                instance.save()

        return instance
