from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic import DetailView,ListView,View
from django.contrib import humanize,messages
from django.core.validators import validate_email,ValidationError
from django.core.mail import send_mail
from SchoolAdmin.models import Notice,SiteSetting
# Create your views here.

def testView(request):
    return render(request,'School/index.html')

# class SchoolIndexView(View):
#     def get(self,request):
#         notice = Notice.objects.all().order_by('-noticeDate'[0:5])

