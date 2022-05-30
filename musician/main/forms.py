from django import forms
from .models import Compositions, Perfomances, Genre, Authors
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PerfomanceForm(forms.ModelForm):
    class Meta:
        model = Perfomances
        fields = ('user', 'composition', 'path', 'datetime', 'is_ideal')

    def __init__(self, *args, **kwargs):
        super(PerfomanceForm, self).__init__(*args, **kwargs)
        self.fields['datetime'].widget = forms.DateInput(attrs={'type': 'date'})
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить исполнение'))


class CompositionForm(forms.ModelForm):
    class Meta:
        model = Compositions
        fields = ('name_composition', 'path', 'genre', 'author')

    def __init__(self, *args, **kwargs):
        super(CompositionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить композицию'))


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name_genre',)

    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить жанр'))


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить жанр'))
