from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

from members.models import Membership
from .forms import ClassForm, RegisterForm, LoginForm


def allusers(request):
    all_users = User.objects.all()
    return render(request, 'members/users.html', {'all_users': all_users})


def profile(request, user_id):
    try:
        retrieved_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404('User does not exist')
    return render(request, 'members/users.html', {'retrieved_user': retrieved_user})


def classes(request, user_id):
    try:
        retrieved_classes = Membership.objects.filter(user=user_id)
    except retrieved_classes.DoesNotExist:
        raise Http404('User does not exist')
    return render(request, 'members/users.html', {'retrieved_classes': retrieved_classes})


class RegisterFormView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'members/register_form.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

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

        form.errors['username'] = form.error_class()

        username = form.data['username']
        password = form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('members:allusers')
        return render(request, 'members/login_form.html', {'form': form})


class ClassFormView(View):
    form_class = ClassForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'members/class_form.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            member = form.save(commit=False)

            type = form.cleaned_data['type']

            member.user = request.user

            member.save()

        return redirect('members:allusers')


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous(),
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator
