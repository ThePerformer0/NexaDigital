from django.db import models

class Realisation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de la réalisation")
    description = models.TextField(verbose_name="Description détaillée du projet")
    client_name = models.CharField(max_length=100, blank=True, verbose_name="Nom du client (optionnel)")
    url_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Lien du site réalisé")
    realization_date = models.DateField(verbose_name="Date de réalisation")

    service_category = models.ForeignKey(
        'services.Service',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Catégorie de service liée"
    )

    technologies_used = models.CharField(max_length=255, blank=True, verbose_name="Technologies utilisées (ex: Django, React, PostgreSQL)")

    image1 = models.ImageField(upload_to='portfolio_images/', blank=True, null=True, verbose_name="Image 1 du projet")
    image2 = models.ImageField(upload_to='portfolio_images/', blank=True, null=True, verbose_name="Image 2 du projet")
    image3 = models.ImageField(upload_to='portfolio_images/', blank=True, null=True, verbose_name="Image 3 du projet")

    class Meta:
        verbose_name = "Réalisation"
        verbose_name_plural = "Réalisations"
        ordering = ['-realization_date']

    def __str__(self):
        return self.title