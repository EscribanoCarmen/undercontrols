# Generated by Django 4.0.4 on 2022-06-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_usuariodatos_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodatos',
            name='direccion',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='app.direccion'),
        ),
        migrations.AlterField(
            model_name='usuariodatos',
            name='metodo_pago',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='app.tarjetacredito'),
        ),
    ]