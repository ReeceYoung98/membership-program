from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import RegisterForm, LoginForm

def allusers(request):
	all_users = User.objects.all()
	return render(request, 'members/users.html', {'all_users': all_users})

def profile(request, user_id):
	try:
		retrieved_user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		raise Http404('User does not exist')
	return render(request, 'members/users.html', {'retrieved_user': retrieved_user,})

class RegisterFormView(View):
	form_class = RegisterForm

	def get(self, request):
		form = self.form_class(None)
		return render(request, 'members/register_form.html', {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']

			user.set_password(password)
			user.save()

			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('members:allusers')

		return render(request, 'members/register_form.html', {'form': form})

class LoginFormView(View):
	form_class = LoginForm

	def get(self, request):
		form = self.form_class(None)
		return render(request, 'members/login_form.html', {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		username = form.data['username']
		password = form.data['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('members:allusers')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')