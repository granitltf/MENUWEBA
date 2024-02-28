from django.forms import ModelForm
from .models import Boire

class BoireForm(ModelForm):
    class Meta:
        model = Boire
        fields = '__all__'
