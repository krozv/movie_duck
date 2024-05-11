from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')				
    else:
        form = CustomUserCreationForm()
    
    context = {
            'form': form,
    }
    return render(request, 'accounts/login.html', context)