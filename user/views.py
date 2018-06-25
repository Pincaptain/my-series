from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import ProfileModel
from series.models import AddedSeriesModel, SeasonModel
import os


class LoginView(View):
    template = os.path.join('user', 'login.html')
    context = {}

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/user/profile')

        self.context['form'] = LoginForm()

        return render(request, self.template, self.context)

    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/user/profile')

        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)

                return HttpResponseRedirect('/user/profile')

        return render(request, self.template, self.context)


# noinspection PyMethodMayBeStatic
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return HttpResponseRedirect('/user/login')

    # noinspection PyUnusedLocal
    def post(self, request):
        return HttpResponseRedirect('/user/logout')


# noinspection PyMethodMayBeStatic
class RegisterView(View):
    template = os.path.join('user', 'register.html')
    context = {}

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/user/profile')

        self.context['form'] = RegisterForm()

        return render(request, self.template, self.context)

    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/user/profile')

        form = RegisterForm(request.POST)

        if form.is_valid():
            obj = User.objects.create_user(form.cleaned_data['username'],
                                           form.cleaned_data['email'],
                                           form.cleaned_data['password'])
            obj.save()

            user = authenticate(request, username=obj.username, password=obj.password)

            if user is not None:
                login(request, user)

                return HttpResponseRedirect('/user/profile')

            return HttpResponseRedirect('/user/login')

        return render(request, self.template, self.context)


class ProfileView(View):
    template = os.path.join('user', 'profile.html')

    addedSeries = AddedSeriesModel.objects.all()
    seasons = SeasonModel.objects.all()
    context = {
        'all_seasons': seasons,
        'added_series': addedSeries
    }

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template, self.context)

        return HttpResponseRedirect('/user/login')

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def post(self, request):
        return HttpResponseRedirect('/user/profile')
