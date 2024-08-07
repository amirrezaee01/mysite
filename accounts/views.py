from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
                user = authenticate(request, username=username, password=password)
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
    else:
        return redirect('/')

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

def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            return redirect('accounts:reset_password', user_id=user.id)
        except User.DoesNotExist:
            error = "No account found with that email address."
            return render(request, 'accounts/password_reset_form.html', {'error': error})
    return render(request, 'accounts/password_reset_form.html')

def reset_password_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        new_password = request.POST.get('password')
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password has been reset successfully!')
        return redirect('accounts:login')
    return render(request, 'accounts/password_reset_confirm.html', {'user_id': user.id})