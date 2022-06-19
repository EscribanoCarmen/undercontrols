# Generated by Django 4.0.4 on 2022-06-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_usuariodatos_delete_usuarioextendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariodatos',
            name='ciudad',
            field=models.CharField(default='Sin Ciudad', max_length=100),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='codigo_seguridad',
            field=models.CharField(default='Sin Codigo', max_length=3),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='fecha_caducidad',
            field=models.CharField(default='Sin Fecha', max_length=100),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='num_tarjeta',
            field=models.CharField(default='Sin Tarjeta', max_length=100),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='provincia',
            field=models.CharField(default='Sin Provincia', max_length=100),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='tarjeta_credito',
            field=models.CharField(choices=[('MasterCard', 'Mastercard'), ('VISA', 'VISA')], default='Sin Pago', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuariodatos',
            name='direccion',
            field=models.CharField(default='C/', max_length=100),
        ),
    ]