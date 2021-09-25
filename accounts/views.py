from django.shortcuts import render
from .forms import CustomUserCreationForm


def register_user(request):

    form = CustomUserCreationForm()

    return render(request, 'accounts/register_user.html', {

        'form': form,

    })


def login_user(request):

    return render(request, 'accounts/login_user.html', {

    })
