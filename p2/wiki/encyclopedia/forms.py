from django import forms
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
      "placeholder": "Page Title", 
      "class": "form-control",
      "style": "max-width: 900px"
    }))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
      "placeholder": "Enter Page Content using Github Markdown",
      "class": "form-control",
      "style": "max-width: 900px"
    }))

class EditPageForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        "placeholder": "Enter Page Content using Github Markdown",
        "class": "form-control",
        "style": "max-width: 900px"
    }))