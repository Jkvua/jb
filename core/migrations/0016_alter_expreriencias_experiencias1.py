# Generated by Django 4.1.1 on 2022-10-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_expreriencias_data_inicio_expreriencias_data_termino_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expreriencias",
            name="experiencias1",
            field=models.TextField(max_length=200),
        ),
    ]
