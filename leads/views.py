from django.shortcuts import render, redirect
from .forms import LeadForm
from services.models import Service

def lead_form(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        initial = {}
        if 'service' in request.GET:
            try:
                service = Service.objects.get(id=request.GET.get('service'))
                initial = {'service': service, 'type': 'QUOTE'}
            except Service.DoesNotExist:
                pass
        form = LeadForm(initial=initial)
    
    return render(request, 'leads/form.html', {'form': form})

def thank_you(request):
    return render(request, 'leads/thank_you.html')