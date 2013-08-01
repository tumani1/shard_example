# coding: utf-8

from django.forms import ModelForm
from apps.accounts.models import *

#############################################################################################################
# Форма ввода пользователя
class AccountForm(ModelForm):

    class Meta:
        model = Accounts
        fields = ('name',)
