from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import PerfilCreationForm, PerfilChangeForm

def signup_view(request):
    if request.method == 'POST':
        form = PerfilCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_detail')
    else:
        form = PerfilCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_detail(request):
    return render(request, 'accounts/profile_detail.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = PerfilChangeForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})
