from django.urls import path,include
from django.contrib.auth.decorators import login_required, permission_required
from .TeachersView import *

urlpatterns = [
    path('Teacher/Add/',login_required(TeacherCreateView.as_view()),name="DashbordTeacherCreate"),
    path('Teacher/<slug:TeacherSlug>',login_required(TeacherDetailView.as_view()),name="DashbordTeacherDetailView"),
    path('Teacher/Update/<slug:TeacherSlug>/',login_required(TeacherUpdateView.as_view()),name="DashbordTeacherUpdate"),
    path('Teacher/Delete/<slug:TeacherSlug>/',login_required(TeacherDeleteView.as_view()),name='TeacherDeleteView'),
]
