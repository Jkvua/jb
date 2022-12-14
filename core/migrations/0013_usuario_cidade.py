# Generated by Django 4.1.1 on 2022-10-27 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_profissional_linkedin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="cidade",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="core.cidade",
            ),
            preserve_default=False,
        ),
    ]
