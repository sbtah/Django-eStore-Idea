from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
#
from django.contrib.auth.decorators import login_required


def register_user(request):

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, (f'User: {username} created.'))
            return redirect('accounts:login')

    return render(request, 'accounts/register_user.html', {

        'form': form,

    })


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, (f'{username}, you were logged in.'))
            return redirect('core:dashboard')
        else:
            messages.info(request, ('Wrong login or password.'))

    return render(request, 'accounts/login_user.html', {

    })


def logout_user(request):

    logout(request)
    messages.success(
        request, ('You Were Logged Out.'))
    return redirect('accounts:login')
