from django.shortcuts import render
from .models import FAQItem


def faq_list(request):
    """Список FAQ"""
    faq_items = FAQItem.objects.filter(is_active=True).order_by('order', '-created_at')
    
    context = {
        'faq_items': faq_items,
    }
    return render(request, 'faq/faq.html', context)
