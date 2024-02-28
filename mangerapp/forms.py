from django.forms import ModelForm
from .models import Manger

class MangerForm(ModelForm):
    class Meta:
        model = Manger
        fields = '__all__'
