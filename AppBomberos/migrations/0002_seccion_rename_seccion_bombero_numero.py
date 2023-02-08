# Generated by Django 4.1.5 on 2023-02-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBomberos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_seccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='bombero',
            old_name='seccion',
            new_name='numero',
        ),
    ]