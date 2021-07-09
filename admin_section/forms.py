from django import forms
import django
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from newspaper_project import models


class Banglades_news(forms.ModelForm):
    
    class Meta:
        model = models.Bangladesh
        fields = '__all__'


class International_news(forms.ModelForm):
    
    class Meta:
        model = models.International
        fields = '__all__'


class Entertainment_news(forms.ModelForm):
    
    class Meta:
        model = models.Entertainment
        fields = '__all__'


class Sports_news(forms.ModelForm):
    
    class Meta:
        model = models.Sports
        fields = '__all__'


class Trade_news(forms.ModelForm):
    
    class Meta:
        model = models.Trade
        fields = '__all__'

