# Generated by Django 2.2.7 on 2019-11-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rut_usuario',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]