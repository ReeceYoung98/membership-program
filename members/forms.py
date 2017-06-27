from django.contrib.auth.models import User
from django import forms

from members.models import Membership


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True

    class Meta:
        model = User
        fields = ['username', 'password']


class ClassForm(forms.ModelForm):
    type = forms.CheckboxSelectMultiple()

    class Meta:
        model = Membership
        fields = ['type']
