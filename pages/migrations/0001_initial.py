# Generated by Django 4.2.21 on 2025-05-20 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Nom du client')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Entreprise du client (optionnel)')),
                ('content', models.TextField(verbose_name='Contenu du témoignage')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='testimonials_photos/', verbose_name='Photo du client (optionnel)')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Note / Étoiles (1 à 5)')),
                ('testimony_date', models.DateField(auto_now_add=True, verbose_name='Date du témoignage')),
                ('is_published', models.BooleanField(default=True, verbose_name='Publier le témoignage')),
            ],
            options={
                'verbose_name': 'Témoignage',
                'verbose_name_plural': 'Témoignages',
                'ordering': ['-testimony_date'],
            },
        ),
    ]
