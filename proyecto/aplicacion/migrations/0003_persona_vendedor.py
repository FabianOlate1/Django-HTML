# Generated by Django 4.0.5 on 2022-06-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_delete_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='vendedor',
            field=models.BooleanField(default=False),
        ),
    ]