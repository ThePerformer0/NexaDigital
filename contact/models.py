from django.db import models

class MessageContact(models.Model):
    STATUS_CHOICES = [
        ('Nouveau', 'Nouveau'),
        ('Lu', 'Lu'),
        ('En cours', 'En cours de traitement'),
        ('Résolu', 'Résolu'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nom du contact")
    email = models.EmailField(verbose_name="Email du contact")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone (optionnel)")
    subject = models.CharField(max_length=200, verbose_name="Sujet du message")
    message = models.TextField(verbose_name="Contenu du message")
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Nouveau',
        verbose_name="Statut du message"
    )

    class Meta:
        verbose_name = "Message de Contact"
        verbose_name_plural = "Messages de Contact"
        ordering = ['-submission_date']

    def __str__(self):
        return f"Message de {self.name} - Sujet: {self.subject} ({self.status})"
