# Generated by Django 5.0.6 on 2024-05-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carWashMng", "0002_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="pic_path",
            field=models.CharField(blank=True, editable=False, max_length=300),
        ),
    ]
