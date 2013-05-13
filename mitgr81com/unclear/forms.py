# -*- coding: utf-8 -*-
from django import forms


class UnclearForm(forms.Form):
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Password to Pass"}))
    passphrase = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Decryption Passphrase"}))
