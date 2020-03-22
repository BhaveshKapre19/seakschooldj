from django.urls import path,include
from django.contrib.auth.decorators import login_required, permission_required
from .views import *
from .NoticeView import (
    NoticeDeleteView,
    NoticeDetailView,
    NoticeUpdateView
)
from .TeachersView import (
    TeacherCreateView,
    TeacherDeleteView,
    TeacherListView,
    TeacherUpdateView,
    TeacherDetailView,
)
from .NonTeachingView import(
    NonTeachingStaffListView,
    NonTeachingStaffCreateView,
    NonTeachingDetailView,
    NonTeachingStaffUpdateView,
    NonTeachingDeleteView
)


app_name="Dashbord"

urlpatterns = [
    path('Login',LoginView,name='Login'),
    path('',login_required(DashbordIndexView.as_view()),name='DashbordIndex'),
    #Teachers Views
    path('Teachers/',login_required(TeacherListView.as_view()),name="DashbordTeacherListView"),
    path('Teacher/Add/',login_required(TeacherCreateView.as_view()),name="DashbordTeacherCreate"),
    path('Teacher/Detail/<slug:TeacherSlug>',login_required(TeacherDetailView.as_view()),name="DashbordTeacherDetailView"),
    path('Teacher/Update/<slug:TeacherSlug>/',login_required(TeacherUpdateView.as_view()),name="DashbordTeacherUpdate"),
    path('Teacher/Delete/<slug:TeacherSlug>/',login_required(TeacherDeleteView.as_view()),name='TeacherDeleteView'),
    #Notices Views
    path('Notice/Detail/<slug:NoticeSlug>/',login_required(NoticeDetailView.as_view()),name="NoticeDetail"),
    path('Notice/Update/<slug:NoticeSlug>/',login_required(NoticeUpdateView.as_view()),name="NoticeUpdate"),
    path('Notice/Delete/<slug:NoticeSlug>/',login_required(NoticeDeleteView.as_view()),name="NoticeDelete"),
    #NTS Views
    path('NTS/',login_required(NonTeachingStaffListView.as_view()),name="NtsListView"),
    path('NTS/Create/',login_required(NonTeachingStaffCreateView.as_view()),name="NtsCreateView"),
    path('NTS/Detail/<slug:NtSlug>/',login_required(NonTeachingDetailView.as_view()),name='NtsDetail'),
    path('NTS/Update/<slug:NtSlug>/',login_required(NonTeachingStaffUpdateView.as_view()),name='NtsUpdate'),
    path('NTS/Delete/<slug:NtSlug>/',login_required(NonTeachingDeleteView.as_view()),name='NtsDelete'),
]
