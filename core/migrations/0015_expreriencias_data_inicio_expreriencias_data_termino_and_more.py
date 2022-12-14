# Generated by Django 4.1.1 on 2022-10-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_expreriencias"),
    ]

    operations = [
        migrations.AddField(
            model_name="expreriencias",
            name="data_inicio",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="expreriencias",
            name="data_termino",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="expreriencias",
            name="experiencias1",
            field=models.TextField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="expreriencias",
            name="experiencias2",
            field=models.TextField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="expreriencias",
            name="experiencias3",
            field=models.TextField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
