from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'examiner/index.html')

@login_required
def upload_registration_data(request):
    return render(request,'examiner/upload_registration_data.html')
@login_required
def upload_paper_data(request):
    return render(request,'examiner/upload_paper_data.html')
@login_required
def make_available(request):
    return render(request,'examiner/make_paper_available.html')
@login_required
def chart(request):
    return render(request,'examiner/charts.html')
@login_required
def table(request):
    return render(request,'examiner/tables.html')