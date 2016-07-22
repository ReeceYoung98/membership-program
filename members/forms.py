from django.contrib.auth.models import User
fromdjango import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
