# Generated by Django 4.0.4 on 2022-06-04 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_tipocamion_botones_alter_tipocamion_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='refCamion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipocamion', unique=True),
        ),
    ]