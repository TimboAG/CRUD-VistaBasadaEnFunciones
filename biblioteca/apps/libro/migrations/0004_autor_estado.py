# Generated by Django 4.2.1 on 2023-05-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_autor_fecha_creacion_libro_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]