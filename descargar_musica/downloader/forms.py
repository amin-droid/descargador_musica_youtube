from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from django.utils.formats import date_format
from django.utils.http import MONTHS
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date, datetime

class VideoLink(forms.Form):
    link = forms.CharField(label='id_search',widget=forms.TextInput(attrs={'class': "form-control"}))
    