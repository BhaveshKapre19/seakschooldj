from django import forms
from  django.contrib.auth.models import User
from .models import Notice,NonTeachingStaff
from django.forms import Textarea,DateInput,EmailField,TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse
from School.models import TeachingStaff

class NoticeForm(forms.ModelForm):
    field_order = ['noticeName','noticeText','noticeDate','noticeIsPublished']

    class Meta:
        model = Notice
        fields = {'noticeName','noticeText','noticeDate','noticeIsPublished'}
        labels = {
            'noticeName':("Notice Title"),
            'noticeText':("Notice Text"),
            'noticeDate':("Date Of Notice"),
            'noticeIsPublished':("Check this to make This Notice published")
        }
        widgets = {
            'noticeText': Textarea(attrs={'cols': 20, 'rows': 5}),
            'noticeDate': DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):

        super(NoticeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('Dashbord:DashbordIndex')
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Add Notice'))

class TeacherCreateForm(forms.ModelForm):
    field_order = [
        'teacherFirstName',
        'teacherLastName',
        'teacherFatherName',
        'teacherSubjectName',
        'teacherDateOfJoining',
        'teacherDateOfBirth',
        'teacherExperince',
        'teacherEmail',
        'teacherNumber',
        'teacherAddress',
        'teacherImage',
    ]
    class Meta:
        model = TeachingStaff
        fields = {'teacherFirstName',
                  'teacherLastName',
                  'teacherFatherName',
                  'teacherSubjectName',
                  'teacherDateOfJoining',
                  'teacherDateOfBirth',
                  'teacherExperince',
                  'teacherEmail',
                  'teacherNumber',
                  'teacherAddress',
                  'teacherImage',
                }
        labels = {
            'teacherFirstName':("First Name"),
            'teacherLastName':("Last Name"),
            'teacherFatherName':("Father Name"),
            'teacherSubjectName':("Subject"),
            'teacherDateOfJoining':('Date Of Joining'),
            'teacherDateOfBirth':('Date Of Birth'),
            'teacherExperince':('Experience'),
            'teacherEmail':("Email Id"),
            'teacherNumber':("Contact Number"),
            'teacherAddress':("Address"),
            'teacherImage':("Image")

        }
        widgets = {
            'teacherAddressteacherAddress': Textarea(attrs={'cols': 20, 'rows': 5}),
            'teacherDateOfJoining': DateInput(attrs={'type':'date'}),
            'teacherDateOfBirth': DateInput(attrs={'type':'date'}),
            'teacherEmail':TextInput(attrs={'type':'email'}),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-teacher-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ('Dashbord:DashbordTeacherCreate')
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Add Teacher'))


class TeacherUpdateForm(forms.ModelForm):
    field_order = [
        'teacherImage',
        'teacherFirstName',
        'teacherLastName',
        'teacherFatherName',
        'teacherSubjectName',
        'teacherExperince',
        'teacherEmail',
        'teacherAddress',
    ]
    class Meta:
        model = TeachingStaff
        fields = {'teacherFirstName',
                  'teacherLastName',
                  'teacherFatherName',
                  'teacherSubjectName',
                  'teacherExperince',
                  'teacherEmail',
                  'teacherNumber',
                  'teacherAddress',
                  'teacherImage',
                }
        labels = {
            'teacherFirstName':("First Name"),
            'teacherLastName':("Last Name"),
            'teacherFatherName':("Father Name"),
            'teacherSubjectName':("Subject"),
            'teacherExperince':('Experience'),
            'teacherEmail':("Email Id"),
            'teacherNumber':("Contact Number"),
            'teacherAddress':("Address"),
            'teacherImage':("Image")

        }
        widgets = {
            'teacherAddressteacherAddress': Textarea(attrs={'cols': 20, 'rows': 5}),
            'teacherEmail':TextInput(attrs={'type':'email'}),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-teacher-update-data-form'
        self.helper.form_method = 'post'
        #self.helper.form_action = ('')
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('Update','Update'))


class NoticeUpdateForm(forms.ModelForm):

    field_order = ['noticeName','noticeText','noticeDate','noticeIsPublished']

    class Meta:
        model = Notice
        fields = {'noticeName','noticeText','noticeDate','noticeIsPublished'}
        labels = {
            'noticeName':("Notice Title"),
            'noticeText':("Notice Text"),
            'noticeDate':("Date Of Notice"),
            'noticeIsPublished':("Check this to make This Notice published")
        }
        widgets = {
            'noticeText': Textarea(attrs={'cols': 20, 'rows': 5}),
            'noticeDate': DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):

        super(NoticeUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-notice-update-data-form'
        self.helper.form_method = 'post'
        #self.helper.form_action = reverse('Dashbord:NoticeUpdate')
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Update Notice'))


class NonTeachingStaffCreate(forms.ModelForm):

    field_order = [
        'ntImage',
        'ntFirstName',
        'ntLastName',
        'ntFatherName',
        'ntPost',
        'ntDateOfBirth',
        'ntJoiningDate',
        'ntEmail',
        'ntPhoneNu',
        'ntAddress'
    ]

    class Meta:
        model = NonTeachingStaff
        fields = {
            'ntImage',
            'ntFirstName',
            'ntLastName',
            'ntFatherName',
            'ntPost',
            'ntDateOfBirth',
            'ntJoiningDate',
            'ntEmail',
            'ntPhoneNu',
            'ntAddress'
        }
        labels = {
            'ntImage':("Image"),
            'ntFirstName':("First Name"),
            'ntLastName':("Last Name"),
            'ntFatherName':("Fathers Name"),
            'ntPost':("On Post"),
            'ntDateOfBirth':("Date Of Birth"),
            'ntJoiningDate':("Date Of Joning"),
            'ntEmail':("Email"),
            'ntPhoneNu':("Contact Number"),
            'ntAddress':("Address"),
        }
        widgets = {
            'ntAddress': Textarea(attrs={'cols': 20, 'rows': 5}),
            'ntDateOfBirth': DateInput(attrs={'type':'date'}),
            'ntJoiningDate': DateInput(attrs={'type':'date'}),
            'ntEmail':TextInput(attrs={'type':'email'}),
        }

    def __init__(self, *args, **kwargs):

        super(NonTeachingStaffCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-nonteaching-data-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Add NT'))


class NonTeachingStaffUpdate(forms.ModelForm):

    field_order = [
        'ntImage',
        'ntFirstName',
        'ntLastName',
        'ntFatherName',
        'ntPost',
        'ntDateOfBirth',
        'ntJoiningDate',
        'ntEmail',
        'ntPhoneNu',
        'ntAddress'
    ]

    class Meta:
        model = NonTeachingStaff
        fields = {
            'ntImage',
            'ntFirstName',
            'ntLastName',
            'ntFatherName',
            'ntPost',
            'ntDateOfBirth',
            'ntJoiningDate',
            'ntEmail',
            'ntPhoneNu',
            'ntAddress'
        }
        labels = {
            'ntImage':("Image"),
            'ntFirstName':("First Name"),
            'ntLastName':("Last Name"),
            'ntFatherName':("Fathers Name"),
            'ntPost':("On Post"),
            'ntDateOfBirth':("Date Of Birth"),
            'ntJoiningDate':("Date Of Joning"),
            'ntEmail':("Email"),
            'ntPhoneNu':("Contact Number"),
            'ntAddress':("Address"),
        }
        widgets = {
            'ntAddress': Textarea(attrs={'cols': 20, 'rows': 5}),
            'ntJoiningDate': DateInput(attrs={'type':'date'}),
            'ntEmail':TextInput(attrs={'type':'email'}),
        }

    def __init__(self, *args, **kwargs):

        super(NonTeachingStaffUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-nonteaching-update-data-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Update NT'))