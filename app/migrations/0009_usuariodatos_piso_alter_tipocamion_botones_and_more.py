# Generated by Django 4.0.4 on 2022-06-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_usuariodatos_ciudad_usuariodatos_codigo_seguridad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariodatos',
            name='piso',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tipocamion',
            name='botones',
            field=models.CharField(choices=[('Cero', '0 [+0€]'), ('Cuatro', '4 [+100€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipocamion',
            name='piel_aro',
            field=models.CharField(choices=[('Cuero', 'Cuero [+200€]'), ('Alcántara', 'Alcántara [+150€]'), ('Goma', 'Goma [+150€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipoformula1',
            name='botones',
            field=models.CharField(choices=[('8', '8 [+0€]'), ('15', '15 [+100€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipoformula1',
            name='material_levas',
            field=models.CharField(choices=[('Plastico', 'Plástico [+0€]'), ('Metal', 'Metal [+50€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipoformula1',
            name='numero_levas',
            field=models.CharField(choices=[('Dos', '2 [+50€]'), ('Tres', '3[+150€]'), ('Cuatro', '4 [+200€]')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tipoturismo',
            name='botones',
            field=models.CharField(choices=[('Ocho', '8 [+100€]'), ('Catorce', '14 [+170€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipoturismo',
            name='material_levas',
            field=models.CharField(choices=[('Plastico', 'Plástico [+0€]'), ('Metal', 'Metal [+50€]')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tipoturismo',
            name='numero_levas',
            field=models.CharField(choices=[('Cero', '0 [+0€]'), ('Dos', '2 [+100€]')], max_length=20),
        ),
    ]
