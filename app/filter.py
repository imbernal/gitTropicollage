from django import forms
import django_filters
from .models import *

class CasaFilter(django_filters.FilterSet):
    # superhost = forms.BooleanField()
    class Meta:
        model = Casa
        fields = ['superhost','ciudad' ,'garaje', 'campo' , 'playa' , 'internet' , 'parqueo' , 'piscina' , 'cant_habitaciones']

class HabitacionFilter(django_filters.FilterSet):
    class Meta:
        model = Habitacion
        fields = ['caja_fuerte' , ]