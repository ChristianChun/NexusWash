# Generated by Django 5.0.6 on 2024-07-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carWashMng", "0008_booking_completed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.PositiveIntegerField()),
                ("picture", models.FileField(upload_to="carWash/static/uploads")),
            ],
        ),
    ]
