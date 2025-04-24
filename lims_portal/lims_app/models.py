from django.db import models

# Create your models here.
class student(models.Model):
    def __str__(self):
        return self.student_name
    student_id=models.CharField(max_length=200)
    student_name=models.CharField(max_length=200)
    student_contact=models.CharField(max_length=200)
    student_course=models.TextField()
    active=models.BooleanField(default=True)


