from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du service")
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fas fa-globe")
    display_order = models.PositiveIntegerField(default=0)
    
    # SEO Fields
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

class ServiceBenefit(models.Model):
    service = models.ForeignKey(Service, related_name='benefits', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fas fa-check-circle")

    def __str__(self):
        return f"{self.service.name} - {self.title}"