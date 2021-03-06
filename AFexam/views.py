from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile
# Create your views here.
def home(request):
    if request.user.username:
        return redirect('panel')
    return render(request,'user/index.html')
@login_required
def panel(request):
    user_name = request.user.username
    try:
        d = User.objects.filter(username=user_name).values('id')
        da = Profile.objects.filter(username_id = d[0]['id']).values('title')
        user_title = da[0]['title']
    except:
        return redirect('profile')
    else:
        if user_title == 'Student':
            return redirect('student_home')
        elif user_title == 'Examiner':
            return redirect('examiner_home')
        else:
            return HttpResponse("Something Went Wrong")

    
    return render(request,'examiner/index.html')


    
def about(request):
    return render(request,'user/about.html')
def service(request):
    return render(request,'user/service.html')
def portfolio(request):
    return render(request,'user/portfolio.html')
def contact(request):
    return render(request,'user/contact.html')