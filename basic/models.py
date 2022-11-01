from django.db import models

# Create your models here.

class student(models.Model):
    stdid=models.IntegerField(unique=True)
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    Mname=models.CharField(max_length=20)
    c= [
    ('MCA', 'MCA'),
    ('II', 'IT'),
    ('COMPUTER', 'COMPUTER'),

    ]
    course=models.CharField(max_length=10,choices=c)
    def __str__(self):
        return self.Fname
class marks(models.Model):
    stdid=models.ForeignKey(student,on_delete=models.CASCADE)
    cmark=models.IntegerField()
    cppmark=models.IntegerField()
    pymark=models.IntegerField()

    def __str__(self):
        return self.stdid
