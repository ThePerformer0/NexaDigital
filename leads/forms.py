from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['type', 'service', 'name', 'email', 'phone', 'company', 'message']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }