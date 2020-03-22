from django.contrib import admin
from .models import Student,TeachingStaff
# Register your models here.

@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display = ('sutdentAdmissionNumber','studentFirstName','studentLastName','studentClass','studentSection','studentNumber','studentAddress','studentEmail',)
    list_display_links = ('sutdentAdmissionNumber',)
    list_editable = ('studentNumber','studentSection','studentClass',)
    list_per_page = 30
    list_filter =   ('studentClass','studentSection',)
    prepopulated_fields = {'studentSlug':('studentFirstName','studentFatherName','studentLastName')}
    search_fields = ('studentClass','studentSection','sutdentAdmissionNumber','studentFirstName','studentLastName','studentFatherName','studentMotherName')
    

@admin.register(TeachingStaff)
class TeachingStaffModal(admin.ModelAdmin):
    list_display = ('teacherFirstName','teacherLastName','teacherDateOfJoining','teacherExperince','teacherSlug','teacherEmail',)
    list_display_links = ('teacherFirstName','teacherSlug')
    list_per_page = 20
    list_filter = ('teacherFirstName','teacherLastName','teacherExperince',)
    search_fields = ('teacherFirstName','teacherLastName','teacherSubjectName',)
    prepopulated_fields = {'teacherSlug':('teacherFirstName','teacherLastName','teacherFatherName','teacherDateOfJoining')}
