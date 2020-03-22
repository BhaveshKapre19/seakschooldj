from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import SchoolAdminUser,Notice,NonTeachingStaff
from School.models import TeachingStaff
from django.utils.text import slugify
from datetime import datetime

import string
import random

def randomStringGenrator(length=32):
    character_set =  string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        slugAdmin = slugify(instance.first_name+" "+instance.last_name+" "+str(datetime.now())+" "+randomStringGenrator(64))
        SchoolAdminUser.objects.create(user=instance,slug=slugAdmin)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    pass


@receiver(post_save,sender=TeachingStaff)
def create_teacher(sender,instance,created,**kwargs):
    if created:
        slugTeacher = slugify(instance.teacherFirstName+" "+instance.teacherFatherName+" "+instance.teacherLastName+" "+str(datetime.now())+" "+randomStringGenrator(32))
        instance.teacherSlug = slugTeacher
        print(slugTeacher)
        instance.save()

@receiver(post_save,sender=TeachingStaff)
def save_teacher(sender,instance,**kwargs):
    pass



@receiver(post_save,sender=Notice)
def create_notice(sender,instance,created,**kwargs):
    if created:
        slugNotice = slugify(instance.noticeName+" "+randomStringGenrator(32)+str(datetime.now()))
        instance.noticeSlug = slugNotice
        #print(slugTeacher)
        instance.save()

@receiver(post_save,sender=Notice)
def save_notice(sender,instance,**kwargs):
    pass


@receiver(post_save,sender=NonTeachingStaff)
def create_nonteachingstaff(sender,instance,created,**kwargs):
    if created:
        slugNt = slugify(instance.ntFirstName+" "+instance.ntFatherName+" "+instance.ntLastName+" "+randomStringGenrator(32)+str(datetime.now()))
        instance.ntSlug = slugNt
        instance.save()

@receiver(post_save,sender=Notice)
def save_nonteachingstaff(sender,instance,**kwargs):
    pass