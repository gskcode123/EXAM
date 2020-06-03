from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse

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

@login_required
def profile(request):
    current_user = request.user.username
    try:
        d = User.objects.filter(username=current_user).values('id')
        da = Profile.objects.filter(username_id = d[0]['id']).values('title')
        user_title = da[0]['title']
        
        
    except:
        if request.method == 'POST':
            title = request.POST.get('title')
            father_name = request.POST['father_name']
            mother_name = request.POST['mother_name']
            date_of_birth = request.POST.get('birthDate')
            gender = request.POST.get('gender')
            address1 = request.POST['street']
            address2 = request.POST['additional']
            address = address1 + address2
            zip_code = request.POST['zip']
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country') 
            code = request.POST.get('code')
            number = request.POST['phone']
            id = User.objects.filter(username=current_user).values('id')
            data = Profile(title=title,father_name = father_name, mother_name = mother_name, date_of_birth = date_of_birth,gender=gender,address=address,zip_code=zip_code,city=city,state = state,country=country,code=code,number=number,username_id=id[0]['id']) 
            data.save()
            return redirect('home')
        
    else:
        return redirect('home')
    
    return render(request,'user/profile.html',{'current_user':current_user})