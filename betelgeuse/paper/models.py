from django.db import models

# Create your models here.


class Subtitle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    bw_positive = models.ImageField()
    color_positive = models.ImageField()
    date_capture = models.DateField()


class Report(models.Model):
    date = models.DateField()
    file = models.FileField()


class Additional(models.Model):
    passepartout = models.BooleanField()
    year_restoration = models.PositiveIntegerField()
    thickness = models.PositiveIntegerField()
    ph = models.DecimalField(max_digits=5, decimal_places=3)
    reports = models.ManyToManyField(Report)


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Structure(models.Model):
    hertzberg = models.ImageField(blank=True, null=True)
    graf_c = models.ImageField(blank=True, null=True)
    discription = models.ManyToManyField(Material, blank=True)


class Rfa(models.Model):
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class Furie(models.Model):
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class Krs(models.Model):
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class HimInfo(models.Model):
    microscopy = models.ImageField(blank=True, null=True)
    uf = models.ImageField(blank=True, null=True)
    express_test = models.ImageField(blank=True, null=True)
    structures = models.ManyToManyField(Structure, blank=True)
    rfa = models.ManyToManyField(Rfa, blank=True)
    ik_furie = models.ManyToManyField(Furie, blank=True)
    krs = models.ManyToManyField(Krs, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Paper(models.Model):
    code = models.CharField(max_length=50, default=None)
    title = models.CharField(max_length=50, default=None)
    year_start = models.PositiveIntegerField(default=None, blank=True, null=True)
    year_end = models.PositiveIntegerField(default=None, blank=True, null=True)
    url = models.URLField(default=None, blank=True, null=True)
    subtitles = models.ManyToManyField(Subtitle, blank=True)
    images = models.ManyToManyField(Image, related_name="paper_images")
    authors = models.ManyToManyField(Author)
    additional = models.OneToOneField(Additional, on_delete=models.CASCADE, blank=True, null=True)
    himinfo = models.OneToOneField(HimInfo, on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.code

    def get_latest_image(self):
        return self.images.latest("id")

    def get_subtitles_as_string(self):
        return ", ".join([subtitle.name for subtitle in self.subtitles.all()])
