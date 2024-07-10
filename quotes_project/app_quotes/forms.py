from django import forms

from .models import Tag, Authors, Quote


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }