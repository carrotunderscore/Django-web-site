from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    return render(request, 'login.html')


def log_in_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # authentication successful, log in the user
            login(request, user)
            # Redirect the user to a different page
            return redirect('profile')
        else:
            # authentication failed, display an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Handle GET requests, such as displaying the login form
        return render(request, 'login.html')


def profile_view(request):
    if request.user.is_authenticated:
        context = {'username': request.user.username}
    else:
        context = {'username': None}
    return render(request, 'profile.html', context)


def sign_up_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            return render(request, 'login.html', {'error_message': 'User already exists'})
        except User.DoesNotExist:
            password = request.POST.get('password')
            userName = request.POST.get('username')
            firstName = request.POST.get('firstname')
            lastName = request.POST.get('lastname')

            user = User.objects.create_user(userName, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()

        return render(request, 'login.html')

    else:
        # Handle GET requests or other methods
        return HttpResponse("This view only accepts POST requests")


def signup_view(request):
    return render(request, 'signup_page.html')
