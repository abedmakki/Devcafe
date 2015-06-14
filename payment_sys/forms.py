from django import forms
from market.models import AppTransactions
from django.contrib.auth.models import User


class Transactions(forms.ModelForm):
    class Meta:
        model = AppTransactions
    )