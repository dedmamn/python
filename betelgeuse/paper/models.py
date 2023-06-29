from django.db import models
from django.utils import timezone
from .tools import *


# Create your models here.
class Subtitle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HimImage(models.Model):
    microscopy = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)
    uf = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)
    express_test = models.ImageField(upload_to=himInfo_upload_path, blank=True, null=True)


class Paper(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year_start = models.PositiveIntegerField(default=None, blank=True, null=True)
    year_end = models.PositiveIntegerField(default=None, blank=True, null=True)
    url = models.URLField(default=None, blank=True, null=True)
    subtitles = models.ManyToManyField(Subtitle, default=None, blank=True)
    authors = models.ManyToManyField(Author)
    year_restoration = models.PositiveIntegerField(default=None, blank=True, null=True)
    passepartout = models.BooleanField()
    thickness = models.PositiveIntegerField(default=None, blank=True, null=True)
    ph = models.DecimalField(max_digits=5, decimal_places=3, default=None, blank=True, null=True)
    himinfo = models.OneToOneField(HimImage, on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.code

    def get_latest_image(self):
        latest_paper_image = self.image_set.order_by("-date_capture").first()
        if latest_paper_image:
            return latest_paper_image.color_positive

    def get_subtitles_as_string(self):
        return ", ".join([subtitle.name for subtitle in self.subtitles.all()])


class Image(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="image_set")
    bw_positive = models.ImageField(upload_to=image_upload_path)
    color_positive = models.ImageField(upload_to=image_upload_path)
    date_capture = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Image {self.id}"


class Report(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="report_set")
    date = models.DateField()
    file = models.FileField(upload_to=report_upload_path)


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
    image = models.ImageField(upload_to=rfa_upload_path)
    txt = models.FileField(upload_to=rfa_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class FurieResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="furie_set")
    image = models.ImageField(upload_to=furie_upload_path)
    txt = models.FileField(upload_to=furie_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class KrsResearch(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="krs_set")
    image = models.ImageField(upload_to=krs_upload_path)
    txt = models.FileField(upload_to=furie_upload_path, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
