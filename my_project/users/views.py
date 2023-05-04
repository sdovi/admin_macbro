from django.shortcuts import render, redirect
from .forms import UsersForm


def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('btn3')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UsersForm()
    return render(request, 'register.html', {'form': form})