# Generated by Django 4.2.2 on 2023-07-08 11:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import paper.tools


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Paper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=50)),
                (
                    "year_start",
                    models.PositiveIntegerField(blank=True, default=None, null=True),
                ),
                (
                    "year_end",
                    models.PositiveIntegerField(blank=True, default=None, null=True),
                ),
                ("url", models.URLField(blank=True, default=None, null=True)),
                (
                    "subtitle",
                    models.CharField(blank=True, default=None, max_length=100),
                ),
                (
                    "year_restoration",
                    models.PositiveIntegerField(blank=True, default=None, null=True),
                ),
                ("passepartout", models.BooleanField()),
                (
                    "thickness",
                    models.PositiveIntegerField(blank=True, default=None, null=True),
                ),
                (
                    "ph",
                    models.DecimalField(
                        blank=True,
                        decimal_places=3,
                        default=None,
                        max_digits=5,
                        null=True,
                    ),
                ),
                ("authors", models.ManyToManyField(to="paper.author")),
            ],
        ),
        migrations.CreateModel(
            name="StructureResearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hertzberg",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=paper.tools.structure_upload_path,
                    ),
                ),
                (
                    "graf_c",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=paper.tools.structure_upload_path,
                    ),
                ),
                (
                    "discription",
                    models.ManyToManyField(blank=True, to="paper.material"),
                ),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="structure_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RfaResearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to=paper.tools.rfa_upload_path)),
                (
                    "txt",
                    models.FileField(
                        blank=True, null=True, upload_to=paper.tools.rfa_upload_path
                    ),
                ),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rfa_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("file", models.FileField(upload_to=paper.tools.report_upload_path)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="report_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KrsResearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to=paper.tools.krs_upload_path)),
                (
                    "txt",
                    models.FileField(
                        blank=True, null=True, upload_to=paper.tools.furie_upload_path
                    ),
                ),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="krs_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bw_positive",
                    models.ImageField(upload_to=paper.tools.image_upload_path),
                ),
                (
                    "color_positive",
                    models.ImageField(upload_to=paper.tools.image_upload_path),
                ),
                ("date_capture", models.DateField(default=django.utils.timezone.now)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HimImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "microscopy",
                    models.ImageField(
                        blank=True, null=True, upload_to=paper.tools.himInfo_upload_path
                    ),
                ),
                (
                    "uf",
                    models.ImageField(
                        blank=True, null=True, upload_to=paper.tools.himInfo_upload_path
                    ),
                ),
                (
                    "express_test",
                    models.ImageField(
                        blank=True, null=True, upload_to=paper.tools.himInfo_upload_path
                    ),
                ),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="him_image",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FurieResearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to=paper.tools.furie_upload_path)),
                (
                    "txt",
                    models.FileField(
                        blank=True, null=True, upload_to=paper.tools.furie_upload_path
                    ),
                ),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="furie_set",
                        to="paper.paper",
                    ),
                ),
            ],
        ),
    ]
