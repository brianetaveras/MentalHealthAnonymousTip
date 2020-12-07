from django.shortcuts import render
import json
from .models import ResourcesDocument
# Create your views here.

def article(request):
    location = request.GET.get('location') or "US"
    article = ResourcesDocument.objects.values().filter(country_code=location).first()
    context = {
        "article": json.dumps(article)
    }
    return render(request, 'health/article.html', context); 