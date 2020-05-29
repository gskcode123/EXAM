from django.shortcuts import render,redirect


from django.contrib import messages
from . forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'user/register.html',{'form':form})

def success(request):
    return render(request,'user/success.html')

def profile(request):
    return render(request,'user/profile.html')