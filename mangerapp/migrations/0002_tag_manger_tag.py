# Generated by Django 5.0.2 on 2024-02-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_plat', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='manger',
            name='tag',
            field=models.ManyToManyField(to='mangerapp.tag'),
        ),
    ]
