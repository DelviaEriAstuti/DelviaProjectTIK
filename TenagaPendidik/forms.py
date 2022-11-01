from dataclasses import fields
from django.forms import ModelForm
from django import forms
from TenagaPendidik.models import TenagaPendidik
class FormTenagaPendidik(ModelForm):
    class Meta: 
        model = TenagaPendidik
        fields = '__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'nim' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'ttl' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.FileInput({'class':'form-control'}),
        }