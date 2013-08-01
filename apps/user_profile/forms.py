# coding: utf-8

from django.forms import ModelForm, ValidationError
from django.forms.fields import IntegerField
from django.forms.widgets import Select

from apps.user_profile.models import *
from apps.accounts.models import *


#############################################################################################################
# Форма профиля
class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        account = [('', '---------------')]
        o_account = Accounts.objects.all()
        for item in o_account:
            account.append((item.pk, item.name))

        self.fields['user'].widget = Select(choices=account)

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        for k,v in self.cleaned_data.items():
            if not k in self.Meta.fields:
                del cleaned_data[k]

        super(UserProfileForm, self).save(commit=False, *args, **kwargs)

        try:
            UserProfile(**cleaned_data).save()
        except:
             return False

        return True

    class Meta:
        model = UserProfile
        fields = ('user', 'email', 'adress',)
        widgets = {
            'user': Select(),
        }
