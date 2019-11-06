from django import forms
from django.forms import CharField, TextInput, BooleanField


class LoginForm(forms.Form):

    username = CharField(
        error_messages={'required': 'Username / Email tidak boleh kosong'},
        widget=TextInput(attrs={'id': 'username', 'class': 'input1 input50',
                                'placeholder': "Masukkan Username / Email"}),
        required=True,
    )

    password = CharField(
        error_messages={'required': 'Password tidak boleh kosong'},
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'input1 input50',
                                'placeholder': "Masukkan Password"}),
        required=True,
    )

    remember_me = BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'mr5 fl'}),
        required=False,
    )