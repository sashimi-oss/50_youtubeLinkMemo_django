from django.forms import ModelForm
from .models import Link
from django import forms

class LinkForm(ModelForm):
  class Meta:
    model = Link
    fields = ['title', 'link', 'category']
    widgets = {
      'title':forms.TextInput(),
      'link': forms.TextInput(attrs={'placeholder':'link'})
    }


class WatchForm(ModelForm):
  class Meta:
    model = Link
    fields = ['category']