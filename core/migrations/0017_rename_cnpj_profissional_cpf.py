# Generated by Django 4.1.1 on 2022-10-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_alter_expreriencias_experiencias1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profissional",
            old_name="cnpj",
            new_name="cpf",
        ),
    ]
