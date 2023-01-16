from django.shortcuts import render
from scraping.models import Vacancy
from scraping.forms import FindForm
import datetime 
def home(request):
    form = FindForm()
    lang = request.GET.get("language")
    city = request.GET.get("city")
    qs = []
    if city or lang:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if lang:
            _filter['language__slug'] = lang
        qs = Vacancy.objects.filter(**_filter)
    _context = {"object_list": qs,'form':form}
    return render(request, 'scraping/home.html', _context)