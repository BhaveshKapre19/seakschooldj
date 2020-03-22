from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
def NonTeachingStaffImageUpload(instance,filename):
    return 'NonTeachingStaff/{0}/{1}'.format(instance.ntSlug,filename)

def SiteLogoImagesUploadPath(instance,filename):
    return 'SiteImages/{0}'.format(filename)

def UserImageUploadPath(instance,filename):
    return 'UserImage/{0}/{1}'.format(instance.userSlug,filename)

class NonTeachingStaff(models.Model):
    ntFirstName = models.CharField(max_length=100)
    ntLastName = models.CharField(max_length=100)
    ntFatherName = models.CharField(max_length=100)
    ntPost = models.CharField(max_length=100)
    ntImage = models.ImageField(upload_to=NonTeachingStaffImageUpload,max_length=1000)
    ntDateOfBirth = models.DateField(null=True)
    ntJoiningDate = models.DateField(default=datetime.now())
    ntSlug = models.SlugField()
    ntEmail = models.EmailField(null=True)
    ntPhoneNu = models.IntegerField(max_length=11,default=0)
    ntAddress = models.TextField(max_length=300,default="null")


    class Meta:
        verbose_name = ("Non Teaching Staff")
        verbose_name_plural = ("Non Teaching Staff")
    
    def __str__(self):
        return self.ntFirstName

class Notice(models.Model):
    noticeName = models.CharField(max_length=255)
    noticeText = models.CharField(max_length=255)
    noticeDate = models.DateField(default=datetime.now())
    noticeAssocFile = models.FileField(null=True,default='null')
    noticeSlug = models.SlugField(max_length=255)
    noticeIsPublished = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Notice")
        verbose_name_plural = ("Notices")
    
    def __str__(self):
        return self.noticeText
    
    def get_absolute_url(self):
        return reverse("Dashbord:NoticeDetail", kwargs={"NoticeSlug": self.noticeSlug})

class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=150)
    siteLogo = models.ImageField(upload_to=SiteLogoImagesUploadPath)
    siteBannerImages = models.ImageField(upload_to=SiteLogoImagesUploadPath)
    sitePrincipalMessage = models.CharField(max_length=200)
    siteDirectorMessage = models.CharField(max_length=200)
    priPhoto = models.ImageField(upload_to=SiteLogoImagesUploadPath)
    DirPhoto = models.ImageField(upload_to=SiteLogoImagesUploadPath)

    class Meta:
        verbose_name = ("Site Setting")
        verbose_name_plural = ("Site Settings")
    
    def __str__(self):
        return self.siteTitle

class SchoolAdminUser(models.Model):
    userAdmin = models.OneToOneField(User,on_delete=models.CASCADE)
    userProfile = models.ImageField(upload_to=UserImageUploadPath)
    userSlug = models.SlugField()

    class Meta:
        verbose_name = ('Admin User')
        verbose_name_plural = ('Admin User')
    
    def __str__(self):
        return self.userAdmin.first_name
    
