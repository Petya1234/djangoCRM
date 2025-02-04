from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name' 
        )
        labels = {
            'email' : _('Email'),
            'username' : _('Username'),
            'first_name' : _('First name'),
            'last_name' : _('Last name')
        }