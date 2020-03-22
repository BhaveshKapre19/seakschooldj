from django.views.generic import DeleteView,DetailView,ListView,CreateView,UpdateView
from .models import Notice
from django.shortcuts import render,redirect,reverse,get_object_or_404
from .forms import *
from django.utils.text import slugify
from .signal import randomStringGenrator
from datetime import datetime


class NoticeDetailView(DetailView):
    model = Notice
    context_object_name = 'Notice'
    slug_url_kwarg = 'NoticeSlug'
    query_pk_and_slug = True
    template_name = 'Admin/Notices/NoticeDetailView.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['NoticeSlug']
        obj = get_object_or_404(Notice,noticeSlug=slug)
        return obj
    
class NoticeUpdateView(UpdateView):
    model = Notice
    form_class = NoticeUpdateForm
    slug_url_kwarg = 'NoticeSlug'
    query_pk_and_slug = True
    template_name = 'Admin/Notices/NoticeUpdateView.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['NoticeSlug']
        obj = get_object_or_404(Notice,noticeSlug=slug)
        return obj

    def form_valid(self,form):
        form.instance.noticeSlug = slugify(form.instance.noticeName+" "+randomStringGenrator(32)+" "+str(datetime.now()))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('Dashbord:DashbordIndex')


class NoticeDeleteView(DeleteView):
    model = Notice
    slug_url_kwarg='NoticeSlug'
    query_pk_and_slug = True
    template_name='Admin/Notices/NoticeDeleteView.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['NoticeSlug']
        obj = get_object_or_404(Notice,noticeSlug=slug)
        return obj
    
    def get_success_url(self):
        return reverse('Dashbord:DashbordIndex')

