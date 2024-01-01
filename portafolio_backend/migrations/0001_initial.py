# Generated by Django 4.2.8 on 2024-01-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("titulo", models.CharField(max_length=120)),
                ("descripcion", models.TimeField()),
                ("imagen", models.ImageField(max_length=2400, upload_to="")),
                ("link", models.URLField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
    ]