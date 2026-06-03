from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account was created.')
            return redirect('product_list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
