# Generated by Django 5.0.2 on 2024-02-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_boisson', models.CharField(max_length=200, null=True)),
                ('taille_boisson', models.CharField(max_length=20, null=True)),
                ('prix_boisson', models.FloatField(null=True)),
            ],
        ),
    ]
