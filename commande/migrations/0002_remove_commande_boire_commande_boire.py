# Generated by Django 5.0.2 on 2024-02-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boireapp', '0001_initial'),
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='boire',
        ),
        migrations.AddField(
            model_name='commande',
            name='boire',
            field=models.ManyToManyField(to='boireapp.boire'),
        ),
    ]