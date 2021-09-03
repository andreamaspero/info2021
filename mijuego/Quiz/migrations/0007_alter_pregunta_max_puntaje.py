# Generated by Django 3.2.4 on 2021-09-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_pregunta_max_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=130, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
    ]