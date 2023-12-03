from django.forms import forms
from crud.models import Cliente

class Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'idade')


