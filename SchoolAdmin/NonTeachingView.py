from django.views.generic import DeleteView,DetailView,ListView,CreateView,UpdateView
from .models import NonTeachingStaff
from django.shortcuts import render,redirect,reverse,get_object_or_404
from .forms import *
from django.utils.text import slugify
from .signal import randomStringGenrator
from datetime import datetime

class NonTeachingStaffListView(ListView):
    model = NonTeachingStaff
    queryset = NonTeachingStaff.objects.all()
    context_object_name = 'NonTeachingStaff'
    template_name = 'Admin/NonTeaching/NonTeachingStaffList.html'
    paginate_by = 1



class NonTeachingDetailView(DetailView):
    model = TeachingStaff
    context_object_name = 'Nts'
    slug_url_kwarg = 'NtSlug'
    query_pk_and_slug = True
    template_name = 'Admin/NonTeaching/NtDetail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['NtSlug']
        obj = get_object_or_404(NonTeachingStaff,ntSlug=slug)
        return obj




class NonTeachingStaffCreateView(CreateView):
    model = NonTeachingStaff
    form_class = NonTeachingStaffCreate
    context_object_name = 'NonTeachingStaff'
    template_name = 'Admin/NonTeaching/NtCreateView.html'

    def get_success_url(self):
        return reverse('Dashbord:NtsListView')



class NonTeachingStaffUpdateView(UpdateView):
    model = NonTeachingStaff
    form_class = NonTeachingStaffUpdate
    template_name = 'Admin/NonTeaching/NtUpdateView.html'
    slug_url_kwarg = 'NtSlug'
    query_pk_and_slug = True

    def get_object(self, queryset=None):
        slug = self.kwargs['NtSlug']
        obj = get_object_or_404(NonTeachingStaff,ntSlug=slug)
        return obj
    
    def form_valid(self,form):
        form.instance.ntSlug = slugify(form.instance.ntFirstName+" "+form.instance.ntFatherName+" "+form.instance.ntLastName+" "+randomStringGenrator(32)+" "+str(datetime.now()))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('Dashbord:NtsListView')



class NonTeachingDeleteView(DeleteView):
    model = NonTeachingStaff
    slug_url_kwarg = 'NtSlug'
    query_pk_and_slug = True
    template_name = 'Admin/NonTeaching/NtDeleteView.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['NtSlug']
        obj = get_object_or_404(NonTeachingStaff,ntSlug=slug)
        return obj
    
    def get_success_url(self):
        return reverse('Dashbord:NtsListView')
