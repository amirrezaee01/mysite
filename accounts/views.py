from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get('identifier')
            password = form.cleaned_data.get('password')

            user = None
            if '@' in identifier:
                try:
                    user_obj = User.objects.get(email=identifier)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            else:
                user = authenticate(username=identifier, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username, email, or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomAuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CustomUserCreationForm()
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
