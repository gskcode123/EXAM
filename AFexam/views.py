from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.user.username:
        return redirect('panel')
    return render(request,'user/index.html')
@login_required
def panel(request):
    return render(request,'examiner/index.html')