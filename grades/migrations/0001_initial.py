# Generated by Django 4.1.3 on 2022-11-09 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "period",
                    models.CharField(
                        choices=[
                            ("MANHÃ", "Matutino"),
                            ("TARDE", "Vespertino"),
                            ("NOITE", "Noturno"),
                        ],
                        default="MANHÃ",
                        max_length=20,
                    ),
                ),
                ("class_name", models.CharField(max_length=30, unique=True)),
                ("grade", models.CharField(max_length=30)),
                (
                    "subjects",
                    models.ManyToManyField(
                        related_name="grades", to="subjects.subject"
                    ),
                ),
            ],
        ),
    ]
