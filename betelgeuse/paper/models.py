from taggit.managers import TaggableManager
from django.db import models
from django.utils import timezone
from .tools import *
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Paper(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year_start = models.PositiveIntegerField(default=None, blank=True, null=True)
    year_end = models.PositiveIntegerField(default=None, blank=True, null=True)
    url = models.URLField(default=None, blank=True, null=True)
    subtitle = models.CharField(max_length=100, default=None, blank=True)
    authors = models.ManyToManyField(Author)
    year_restoration = models.PositiveIntegerField(default=None, blank=True, null=True)
    passepartout = models.BooleanField()
    thickness = models.PositiveIntegerField(default=None, blank=True, null=True)
    ph = models.DecimalField(max_digits=5, decimal_places=3, default=None, blank=True, null=True)

    def __str__(self):
        return self.code

    def get_latest_image(self):
        latest_paper_image = self.image_set.order_by("-date_capture").first()
        if latest_paper_image:
            return latest_paper_image.color_positive

    # def get_subtitles_as_string(self):
    #     return ", ".join([subtitle.name for subtitle in self.subtitles.all()])

    def get_authors_as_string(self):
        return ", ".join([author.name for author in self.authors.all()])

    def get_years_as_string(self):
        year_start = str(self.year_start) if self.year_start is not None else ""
        year_end = str(self.year_end) if self.year_end is not None else ""
        return " - ".join([year_start, year_end])

    def get_absolute_url(self):
        return reverse("paper-update", kwargs={"pk": self.pk})


class HimImage(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="him_image")
    microscopy = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)
    uf = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)
    express_test = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)


class Image(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="image_set")
    bw_positive = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    color_positive = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    date_capture = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"


class Report(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="report_set")
    date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to=report_upload_path, blank=True, null=True)


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StructureResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="structure_set")
    hertzberg = models.ImageField(upload_to=structure_upload_path, blank=True, null=True)
    graf_c = models.ImageField(upload_to=structure_upload_path, blank=True, null=True)
    discription = models.ManyToManyField(Material, blank=True)


class RfaResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="rfa_set")
    image = models.ImageField(upload_to=rfa_upload_path, blank=True, null=True)
    txt = models.FileField(upload_to=rfa_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class FurieResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="furie_set")
    image = models.ImageField(upload_to=furie_upload_path, blank=True, null=True)
    txt = models.FileField(upload_to=furie_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Furie paper - {self.paper.code} research"


class KrsResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="krs_set")
    image = models.ImageField(upload_to=krs_upload_path, blank=True, null=True)
    txt = models.FileField(upload_to=krs_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
