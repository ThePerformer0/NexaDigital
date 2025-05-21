from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Temoignage(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Nom du client")
    company_name = models.CharField(max_length=100, blank=True, verbose_name="Entreprise du client (optionnel)")
    content = models.TextField(verbose_name="Contenu du témoignage")
    photo = models.ImageField(upload_to='testimonials_photos/', blank=True, null=True, verbose_name="Photo du client (optionnel)")
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Note / Étoiles (1 à 5)"
    )
    testimony_date = models.DateField(auto_now_add=True, verbose_name="Date du témoignage")
    is_published = models.BooleanField(default=True, verbose_name="Publier le témoignage")

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-testimony_date']

    def __str__(self):
        return f"Témoignage de {self.author_name} ({self.company_name or 'N/A'})"
