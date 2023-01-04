from django.shortcuts import render
from scraping.models import Vacancy
import datetime 
def home(request):
    date = datetime.datetime.now().date()
    lang = request.GET.get("language")
    city = request.GET.get("city")
    qs = []
    if city or lang:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if lang:
            _filter['language__name'] = lang
        qs = Vacancy.objects.filter(**_filter)
    name = 'Nikita'
    city = 'Moscow'
    _context = {'date': date, 'name': name, 'town':city, "object_list": qs}
    return render(request, 'scraping/home.html', _context)