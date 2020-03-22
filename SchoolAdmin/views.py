from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth,messages
from django.views import View
from .models import NonTeachingStaff,Notice
from datetime import datetime
from .forms import NoticeForm


# Create your views here.
# def testView(request):
#     return render(request,'Admin/index.html')


def LoginView(request):
    form = AuthenticationForm()
    if request.POST:
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request, 'Succssfully login')
                return redirect('Dashbord:DashbordIndex')
            else:
                messages.error(request,'No User Found')
                return redirect('login')
        else:
            messages.error(request, 'Error')
            return render(request, 'LoginDashbord.html', {'form': form})
    else:
        return render(request, 'LoginDashbord.html', {'form': form})





class DashbordIndexView(View):

    @method_decorator(login_required)
    def get(self,request):
        notice = Notice.objects.all().order_by('-noticeDate')
        form = NoticeForm()
        context = {'notices':notice,'formNoticeCreate':form}
        return render(request,'Admin/index.html',context)

    @method_decorator(login_required)
    def post(self,request):
        form = NoticeForm()
        formNotice = NoticeForm(request.POST)
        if formNotice.is_valid():
            formNotice.save()
        else:
            messages.success(request, 'Some Error Occured By Your Side')
            redirect('Dashbord:DashbordIndex')
        notice = Notice.objects.all().order_by('-noticeDate')
        context = {'notices':notice,'formNoticeCreate':form}
        return render(request,'Admin/index.html',context)


