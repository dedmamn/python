# Generated by Django 4.2.2 on 2023-06-12 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Additional",
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
                ("passepartout", models.BooleanField()),
                ("year_restoration", models.PositiveIntegerField()),
                ("thickness", models.PositiveIntegerField()),
                ("ph", models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
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
            name="Furie",
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
                ("image", models.ImageField(upload_to="")),
                ("text", models.FileField(blank=True, null=True, upload_to="")),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HimInfo",
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
                ("microscopy", models.ImageField(blank=True, null=True, upload_to="")),
                ("uf", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "express_test",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                ("ik_furie", models.ManyToManyField(blank=True, to="paper.furie")),
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
                ("bw_positive", models.ImageField(upload_to="")),
                ("color_positive", models.ImageField(upload_to="")),
                ("date_capture", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Krs",
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
                ("image", models.ImageField(upload_to="")),
                ("text", models.FileField(blank=True, null=True, upload_to="")),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
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
                ("date", models.DateField()),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Rfa",
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
                ("image", models.ImageField(upload_to="")),
                ("text", models.FileField(blank=True, null=True, upload_to="")),
                ("parameters", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubTitle",
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
            name="Structure",
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
                ("hertzberg", models.ImageField(blank=True, null=True, upload_to="")),
                ("graf_c", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "discription",
                    models.ManyToManyField(blank=True, to="paper.material"),
                ),
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
                ("code", models.CharField(default=None, max_length=50)),
                ("title", models.CharField(default=None, max_length=50)),
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
                    "additional",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paper.additional",
                    ),
                ),
                ("authors", models.ManyToManyField(to="paper.author")),
                (
                    "himinfo",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paper.himinfo",
                    ),
                ),
                ("images", models.ManyToManyField(to="paper.image")),
                ("subtitles", models.ManyToManyField(blank=True, to="paper.subtitle")),
            ],
        ),
        migrations.AddField(
            model_name="himinfo",
            name="krs",
            field=models.ManyToManyField(blank=True, to="paper.krs"),
        ),
        migrations.AddField(
            model_name="himinfo",
            name="rfa",
            field=models.ManyToManyField(blank=True, to="paper.rfa"),
        ),
        migrations.AddField(
            model_name="himinfo",
            name="structures",
            field=models.ManyToManyField(blank=True, to="paper.structure"),
        ),
        migrations.AddField(
            model_name="additional",
            name="reports",
            field=models.ManyToManyField(to="paper.report"),
        ),
    ]
