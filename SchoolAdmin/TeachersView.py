from django.views.generic import DeleteView,DetailView,ListView,CreateView,UpdateView
from School.models import TeachingStaff
from django.shortcuts import render,redirect,reverse,get_object_or_404
from .forms import *
from django.utils.text import slugify
from .signal import randomStringGenrator
from datetime import datetime


class TeacherListView(ListView):
    model = TeachingStaff
    queryset = TeachingStaff.objects.all()
    template_name = 'Admin/Teacher/TeacherListView.html'
    context_object_name = 'Teacher'
    paginate_by = 1

    def get_context_data(self,**kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        form = NoticeForm()
        context.update({
            'formNoticeCreate':form
        })
        return context

class TeacherDetailView(DetailView):
    model = TeachingStaff
    context_object_name = 'Teacher'
    slug_url_kwarg = 'TeacherSlug'
    query_pk_and_slug = True
    template_name = 'Admin/Teacher/TeacherDetailView.html'
    #queryset = TeachingStaff.objects.all()

    def get_object(self, queryset=None):
        slug = self.kwargs['TeacherSlug']
        obj = get_object_or_404(TeachingStaff,teacherSlug=slug)
        return obj

    def get_context_data(self,**kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        form = NoticeForm()
        context.update({
            'formNoticeCreate':form
        })
        return context

class TeacherCreateView(CreateView):
    model = TeachingStaff
    form_class = TeacherCreateForm
    template_name = 'Admin/Teacher/TeacherCreateView.html'

    def get_success_url(self):
        return reverse('Dashbord:DashbordTeacherListView')

    # def form_valid(self, form):
    #     form.instance.TeacherSlug = self.request.user
    #     return super().form_valid(form)


class TeacherUpdateView(UpdateView):
    model = TeachingStaff
    form_class = TeacherUpdateForm
    template_name = 'Admin/Teacher/TeacherUpdateView.html'
    slug_url_kwarg = 'TeacherSlug'
    query_pk_and_slug = True
    #success_url = 'Dashbord:DashbordTeacherListView'

    def get_object(self, queryset=None):
        slug = self.kwargs['TeacherSlug']
        obj = get_object_or_404(TeachingStaff,teacherSlug=slug)
        return obj

    def form_valid(self,form):
        form.instance.ntSlug = slugify(form.instance.teacherFirstName+" "+form.instance.teacherFatherName+" "+form.instance.teacherLastName+" "+randomStringGenrator(32)+" "+str(datetime.now()))
        return super().form_valid(form)
    
    def get_context_data(self,**kwargs):
        context = super(TeacherUpdateView, self).get_context_data(**kwargs)
        form = NoticeForm()
        context.update({
            'formNoticeCreate':form
        })
        return context

    def get_success_url(self):
        return reverse('Dashbord:DashbordTeacherListView')

class TeacherDeleteView(DeleteView):
    model = TeachingStaff
    slug_url_kwarg = 'TeacherSlug'
    query_pk_and_slug = True
    template_name = 'Admin/Teacher/TeacherDeleteView.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['TeacherSlug']
        obj = get_object_or_404(TeachingStaff,teacherSlug=slug)
        return obj
    
    def get_success_url(self):
        return reverse('Dashbord:DashbordTeacherListView')


