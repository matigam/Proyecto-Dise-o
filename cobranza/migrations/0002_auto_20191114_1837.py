# Generated by Django 2.2.7 on 2019-11-14 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cobranza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruta',
            old_name='Fecha_Ruta',
            new_name='fecha_Ruta',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='Propietario',
        ),
        migrations.AddField(
            model_name='ruta',
            name='cobrador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
