from django.contrib import admin
from .models import SchoolAdminUser,NonTeachingStaff,Notice,SiteSetting

# Register your models here.
@admin.register(Notice)
class NoticeModel(admin.ModelAdmin):
    list_display = ('noticeName','noticeText','noticeDate',)
    list_per_page = 5
    list_display_links = ('noticeName',)
    search_fields = ('noticeName','noticeText',)
    prepopulated_fields = {'noticeSlug':('noticeName','noticeDate')}
    list_filter = ('noticeDate',)


@admin.register(NonTeachingStaff)
class NonTeachingStaffModel(admin.ModelAdmin):
    list_display = ('ntFirstName','ntPost','ntJoiningDate','ntImage','ntEmail',)
    list_display_links = ('ntFirstName',)
    search_fields = ('ntFirstName','ntLastName','ntPost',)
    prepopulated_fields = {'ntSlug':('ntFirstName','ntLastName','ntFatherName')}

@admin.register(SiteSetting)
class SiteSettingModel(admin.ModelAdmin):
    list_display = ('siteTitle','siteLogo')

@admin.register(SchoolAdminUser)
class SchoolAdminModal(admin.ModelAdmin):
    list_display = ('userAdmin','userSlug',)