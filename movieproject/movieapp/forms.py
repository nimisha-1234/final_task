from django import forms
from django.forms import NumberInput

from .models import Movie


class MovieForms(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name', 'category', 'desc', 'actor_name', 'release_date', 'img', 'movie_link']

        widgets = {
            'movie_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'actor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'movie_link': forms.URLInput(attrs={'class': 'form-control'}),

        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
