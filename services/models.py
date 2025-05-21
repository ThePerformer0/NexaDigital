from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du service")
    description = models.TextField(verbose_name="Description détaillée du service")
    icon_class = models.CharField(max_length=50, blank=True, null=True, verbose_name="Classe d'icône (ex: 'fa-solid fa-code')")
    is_active = models.BooleanField(default=True, verbose_name="Service actif")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    key_points = models.TextField(blank=True, verbose_name="Points clés / Avantages (un par ligne)")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
