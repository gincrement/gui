# Generated by Django 4.2.4 on 2024-10-10 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0020_rename_input_timeseries_asset_input_timeseries_old")
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="input_timeseries",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.timeseries",
            ),
        )
    ]
