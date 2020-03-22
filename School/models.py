from django.db import models
from django.shortcuts import reverse
# Create your models here.

def studentImageUploadPath(instance,filename):
    return 'StudentsImage/{0}/{1}'.format(instance.studentAdmissionNumber,filename)

def TeacherImageUploadPath(instance,filename):
    return 'Teachers/{0},{1}'.format(instance.teacherFirstName,filename)


class Student(models.Model):
    sutdentAdmissionNumber = models.IntegerField(max_length=10)
    studentFirstName = models.CharField(max_length=100)
    studentLastName = models.CharField(max_length=100)
    studentFatherName = models.CharField(max_length=100)
    studentMotherName = models.CharField(max_length=100)
    studentAddress = models.CharField(max_length=400)
    studentClass = models.IntegerField(max_length=2)
    studentSection = models.CharField(max_length=2)
    studentNumber = models.IntegerField(max_length=10)
    studentSlug = models.SlugField()
    studentPhoto = models.ImageField(upload_to=studentImageUploadPath)
    studentDateOfBirth = models.DateField()
    studentEmail = models.EmailField(null=True)

    class Meta:
        verbose_name=("Student")
        verbose_name_plural=("Students")

    def __str__(self):
        return self.studentFirstName
    
    
class TeachingStaff(models.Model):
    teacherSlug = models.SlugField()
    teacherFirstName = models.CharField(max_length=100)
    teacherLastName = models.CharField(max_length=100)
    teacherSubjectName = models.CharField(max_length=300)
    teacherFatherName = models.CharField(max_length=100)
    teacherDateOfJoining = models.DateField()
    teacherDateOfBirth = models.DateField()
    teacherImage = models.ImageField(upload_to=TeacherImageUploadPath)
    teacherExperince = models.IntegerField(max_length=1)    
    teacherEmail = models.EmailField(null=True)
    teacherNumber = models.IntegerField(max_length=11,null=True)
    teacherAddress = models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name=("Teacher")
        verbose_name_plural=("Teachers")

    def __str__(self):
        return self.teacherFirstName
    
    def get_absolute_url(self):
        return reverse("Dashbord:DashbordTeacherDetailView", kwargs={"TeacherSlug": self.teacherSlug})
    