from django import forms
import django_filters
from .models import *

class CasaFilter(django_filters.FilterSet):
    # superhost = forms.BooleanField()
    class Meta:
        model = Casa
        fields = ['superhost','ciudad' ,'filter_agua_caliente', 'campo' , 'playa' , 'internet' , 'parqueo' , 'filter_bano_privado' , 'filter_caja_fuerte']

