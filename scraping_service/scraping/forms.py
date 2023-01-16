from django import forms 
from .models import City, Lang 
class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False, label="Город")
    language = forms.ModelChoiceField(queryset=Lang.objects.all(), to_field_name='slug', required=False, label="Язык программирования")