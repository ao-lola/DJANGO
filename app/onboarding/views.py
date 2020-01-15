from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from onboarding.forms import SignUpForm

# Create your views here.

def login(request):
  return render(request, 'onboarding/login.html')


def signup(request):
  if request.method == "GET":
    form = UserCreationForm()
    context = { 'form': form,}
    return render(request, 'onboarding/signup.html', context)

  if request.method =="POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = user.objects.create_user(
        username =(form.cleaned_data['username']).casefold(),
        password =form.cleaned_data['password1'],
      )

      messages.success(request, 'Account successfully created. Please, login to dashboard')
      return redirect('signup')

    context = {'form': form}
    return render(request, 'onboarding/signup.html', context)
    return render(request, 'onboarding/signup.html')