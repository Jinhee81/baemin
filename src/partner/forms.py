from django import forms
from django.forms import ModelForm
from .models import Partner

class PartnerForm(ModelForm):
    class Meta :
        model = Partner
        fields = (
            "name",
            "contact",
            "address",
            "description"
        )
        widgets = {
            "name" : forms.TextInput(attrs = {"class":"form-control"}),
            "contact" : forms.TextInput(attrs = {"class":"form-control"}),
            "address" : forms.TextInput(attrs = {"class":"form-control"}),
            "description" : forms.Textarea(attrs = {"class":"form-control"})
        }
