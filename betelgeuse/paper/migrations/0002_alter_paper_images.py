# Generated by Django 4.2.2 on 2023-06-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paper", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="images",
            field=models.ManyToManyField(related_name="paper_images", to="paper.image"),
        ),
    ]