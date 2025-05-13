from django.db import models
from services.models import Service

class Lead(models.Model):
    LEAD_TYPE_CHOICES = [
        ('CONTACT', 'Demande de contact'),
        ('QUOTE', 'Demande de devis'),
        ('MEETING', 'Prise de rendez-vous'),
    ]
    
    type = models.CharField(max_length=10, choices=LEAD_TYPE_CHOICES)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.get_type_display()}"