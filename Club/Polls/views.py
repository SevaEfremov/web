from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lgn
from .forms import SignUpForm, SignInForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def bronb(request):
    return render(request, 'bronb.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                lgn(request, user)
                return redirect('home')  # Переадресация на главную страницу после успешной регистрации
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            lgn(request, user)
        return redirect('home')
        
    else:
        return render(request, 'login.html')