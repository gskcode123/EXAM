from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    zip_code = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    number = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        num = str(self.number)
        return num




