# Generated by Django 2.2.4 on 2020-10-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("management", "0021_auto_20201008_1419")]

    operations = [migrations.AddField(model_name="permission", name="description", field=models.TextField(null=True))]
