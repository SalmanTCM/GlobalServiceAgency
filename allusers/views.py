from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import RegistrationForm


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
