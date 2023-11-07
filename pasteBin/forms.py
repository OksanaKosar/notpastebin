import datetime

from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import Paste, Tag


def get_1_day():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m/%d/%Y")


def get_7_days():
    return (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%m/%d/%Y")


def get_30_days():
    return (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%m/%d/%Y")


def get_90_days():
    return (datetime.datetime.now() + datetime.timedelta(days=90)).strftime("%m/%d/%Y")


def get_180_days():
    return (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%m/%d/%Y")


class PasteForm(forms.ModelForm):
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple,
    )
    EXPIRATION_CHOICES = (
        ("", "Never"),
        (get_1_day, "1 day"),
        (get_7_days, "7 days"),
        (get_30_days, "30 days"),
        (get_90_days, "90 days"),
        (get_180_days, "180 days"),
    )

    expiration_date = forms.DateField(widget=forms.Select(choices=EXPIRATION_CHOICES), required=False)

    class Meta:
        model = Paste
        fields = ['title', 'content', 'tags', 'text_type', 'expiration_date', 'access_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 7})


class PasswordForm(forms.Form):
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword',  'autocomplete': 'off'}),
    )




