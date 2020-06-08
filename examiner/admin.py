from django.contrib import admin
from . models import Subjects,Exams,Questions,Registration_data
# Register your models here.
admin.site.register(Questions)
admin.site.register(Subjects)
admin.site.register(Exams)
admin.site.register(Registration_data)