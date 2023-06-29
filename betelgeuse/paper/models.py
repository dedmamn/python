from django.db import models


# Create your models here.


class Subtitle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Additional(models.Model):
    passepartout = models.BooleanField()
    year_restoration = models.PositiveIntegerField()
    thickness = models.PositiveIntegerField()
    ph = models.DecimalField(max_digits=5, decimal_places=3)


class HimInfo(models.Model):
    microscopy = models.ImageField(blank=True, null=True)
    uf = models.ImageField(blank=True, null=True)
    express_test = models.ImageField(blank=True, null=True)


class Paper(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year_start = models.PositiveIntegerField(default=None, blank=True, null=True)
    year_end = models.PositiveIntegerField(default=None, blank=True, null=True)
    url = models.URLField(default=None, blank=True, null=True)
    subtitles = models.ManyToManyField(Subtitle, default=None, blank=True)
    authors = models.ManyToManyField(Author)
    additional = models.OneToOneField(Additional, on_delete=models.CASCADE, blank=True, null=True)
    himinfo = models.OneToOneField(HimInfo, on_delete=models.CASCADE, blank=True, null=True, default=None)

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
    bw_positive = models.ImageField()
    color_positive = models.ImageField()
    date_capture = models.DateField()

    def __str__(self):
        return f"Image {self.id}"


class Report(models.Model):
    additional = models.ForeignKey(Additional, on_delete=models.CASCADE, related_name="report_set")
    date = models.DateField()
    file = models.FileField()


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Structure(models.Model):
    him_info = models.ForeignKey(HimInfo, on_delete=models.CASCADE, related_name="structure")
    hertzberg = models.ImageField(blank=True, null=True)
    graf_c = models.ImageField(blank=True, null=True)
    discription = models.ManyToManyField(Material, blank=True)


class Rfa(models.Model):
    him_info = models.ForeignKey(HimInfo, on_delete=models.CASCADE, related_name="rfa")
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class Furie(models.Model):
    him_info = models.ForeignKey(HimInfo, on_delete=models.CASCADE, related_name="furie")
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)


class Krs(models.Model):
    him_info = models.ForeignKey(HimInfo, on_delete=models.CASCADE, related_name="krs")
    image = models.ImageField()
    text = models.FileField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
