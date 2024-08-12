from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method== 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})        


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Trying to authenticate user: {username}")  # Debug line
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"User authenticated: {username}")  # Debug line
            login(request, user)
            return redirect('home')
        else:
            print(f"Authentication failed for user: {username}")  # Debug line
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

    
@login_required
def home(request):
    return render(request, 'home.html')