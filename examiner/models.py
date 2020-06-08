from django.db import models

# Create your models here.

class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.subject_name

class Exams(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_code = models.CharField(max_length=10,primary_key=True)
    exam_date = models.DateField(auto_now=True)
    subject_of_exam = models.ForeignKey(Subjects,on_delete=models.CASCADE)

    def __str__(self):
        return self.exam_name

class Questions(models.Model):
    question = models.TextField()
    options1 = models.TextField()
    options2 = models.TextField()
    options3 = models.TextField()
    options4 = models.TextField()
    answer = models.TextField()

    question_of_exam = models.ForeignKey(Exams,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Registration_data(models.Model):
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    data_of_exam = models.ForeignKey(Exams,on_delete=models.CASCADE)

    def __str__(self):
        return self.email