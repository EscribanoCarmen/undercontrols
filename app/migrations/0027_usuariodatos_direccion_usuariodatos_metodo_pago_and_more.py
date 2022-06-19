# Generated by Django 4.0.4 on 2022-06-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_remove_usuariodatos_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariodatos',
            name='direccion',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='app.direccion'),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='metodo_pago',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='app.tarjetacredito'),
        ),
        migrations.AlterField(
            model_name='tipoturismo',
            name='material_levas',
            field=models.CharField(choices=[('Plastico', 'Plástico [+0€]'), ('Metal', 'Metal [+50€]')], max_length=100, null=True),
        ),
    ]