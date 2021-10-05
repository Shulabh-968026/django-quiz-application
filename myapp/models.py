from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Course(models.Model):
    course_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.course_name

class Questions(models.Model):
    quiz=models.ForeignKey(Course,on_delete=models.CASCADE)
    qusestion_text=models.CharField(max_length=1000)
    answer=models.CharField(max_length=300)
    option1=models.CharField(max_length=300)
    option2=models.CharField(max_length=300)
    option3=models.CharField(max_length=300,blank=True)
    option4=models.CharField(max_length=300,blank=True)

    def __str__(self) -> str:
        return self.qusestion_text
