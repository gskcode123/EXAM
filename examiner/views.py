from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv, io
import json
from django.contrib import messages
from . models import Registration_data,Questions,Exams,Subjects
import pandas as pd

# Create your views here.
@login_required
def home(request):
    current_user = request.user.username
    return render(request,'examiner/index.html',{'username':current_user})



@login_required
def make_available(request):
    current_user = request.user.username
    return render(request,'examiner/make_paper_available.html',{'username':current_user})
@login_required
def chart(request):
    current_user = request.user.username
    return render(request,'examiner/charts.html',{'username':current_user})
@login_required
def table(request):
    current_user = request.user.username
    return render(request,'examiner/tables.html',{'username':current_user})

@login_required
def create_exam(request):
    current_user = request.user.username
    current_user = request.user.username
    subjects_data = Subjects.objects.all()
    


   

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        exam_name = request.POST.get('exam_name')
        exam_code = request.POST.get('exam_code')
        
        ss = Subjects.objects.filter(subject_name=subject_name).values('subject_code')
        request.session['exam_name'] = exam_name
        request.session['exam_code'] = exam_code
        request.session['subject_name'] = subject_name
        request.session['subject_code'] = subject_code
        
        
        subject_code_db = ss[0]['subject_code']
        subject_instance = Subjects(subject_name=subject_name,subject_code=subject_code)
        
        
        try:
            data = Exams.objects.create(exam_name=exam_name,exam_code=exam_code,subject_of_exam=subject_instance)
            data.save()
            

            return redirect('upload_registration_data')
        except:
            return HttpResponse("Subject Code not Match")
        
        
        

    return render(request,'examiner/create_exam.html',{'sd':subjects_data,'username':current_user})



@login_required
def upload_registration_data(request):
    

    exam_name = request.session['exam_name']
    exam_c = request.session['exam_code']
    subject_name = request.session['subject_name']
    subject_code = request.session['subject_code']
    template = "examiner/upload_registration_data.html"
    data = Registration_data.objects.all()# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be email,password',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    try:
        csv_file = request.FILES['file']  # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')   
        data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
    
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):

            created = Registration_data.objects.update_or_create(
            email = column[0],
            password = column[1],
            data_of_exam_id = exam_c)
            return redirect('upload_paper_data')

        context = {}
    except:
        return HttpResponse("AN Email Error occured !! No email present previously in Database")

    return render(request,'examiner/upload_registration_data.html',context)


@login_required
def upload_paper_data(request):
    current_user = request.user.username
    
    

    exam_name = request.session['exam_name']
    exam_c = request.session['exam_code']
    subject_name = request.session['subject_name']
    subject_code = request.session['subject_code']
    template = "examiner/upload_paper_data.html"
    data = Questions.objects.all()# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be question,option1,option2,option3,option4,answer',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    try:
        csv_file = request.FILES['file'] 
      # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')   
        data = pd.read_csv(csv_file)
        print(data)
        print(data.iloc[2]['question'])
    
        le = len(data) + 1
        for i in range(0,3):
            question1 = data.iloc[i]['question']
            option1=data.iloc[i]['options1']
            option2=data.iloc[i]['options2']
            option3=data.iloc[i]['options3']
            option4=data.iloc[i]['options4'],
            ans=data.iloc[i]['answer']
            q = Questions.objects.create(question=question1,options1=option1,options2=option2,options3=option3,options4=option4,answer=ans,question_of_exam_id=exam_c)
            return redirect('home')

    except:
        return HttpResponse("You csv file not in required format")


    return render(request,'examiner/upload_paper_data.html',{'username':current_user})