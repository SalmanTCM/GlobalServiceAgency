from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    # Assuming you have a UserProfile model, you can retrieve the user's profile here
    user_profile = request.user.userprofile  # Adjust to your actual model

    # You can also pass other user-related data to the template
    context = {
        'user_profile': user_profile,  # Include user profile data if available
    }

    return render(request, 'profile.html', context)

@csrf_protect
def login_view(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Replace 'profile' with your actual profile URL name
            else:
                form.add_error(None, 'Invalid username or password.')

    else:
        form = LoginForm()  # Create an empty form for GET requests

    return render(request, 'login.html', {'form': form})
