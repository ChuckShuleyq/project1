from django import forms 
from .models import City, Lang 
class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    language = forms.ModelChoiceField(queryset=Lang.objects.all())