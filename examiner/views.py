from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'examiner/index.html')

def upload_registration_data(request):
    return render(request,'examiner/upload_registration_data.html')

def upload_paper_data(request):
    return render(request,'examiner/upload_paper_data.html')

def make_available(request):
    return render(request,'examiner/make_paper_available.html')
def chart(request):
    return render(request,'examiner/charts.html')
def table(request):
    return render(request,'examiner/tables.html')