from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


@login_required
def home(request):
    """
    A funcao esta retornando o template index.html
    @param1: request
    @return: 200: Se o template for retornado com sucesso
    """
    return render(request, 'index.html')


def signup(request):
    """
    A funcao esta criando o usuário
    @param1: request
    @param2: form
    @param3: email
    @param4: username
    @param5: raw_password 
    @param6: user

    @return: 201: Se o usuário for criado
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
