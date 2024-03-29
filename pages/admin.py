
from django.contrib import admin
from pages.models import Otp, Otp_Two, Team, Guide, Temp_Team, Temp_User, Credit
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class GuideResource(resources.ModelResource):
    class Meta:
        model = Guide
        import_id_fields = ('serial_no',)
        exclude = ('id',)
        fields = ('serial_no', 'name', 'emp_id', 'designation', 'domain_1', 'domain_2', 'domain_3',
                  'email', 'myImage', 'vacancy')


class GuideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('serial_no', 'name', 'emp_id', 'designation', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'myImage', 'vacancy')
    ordering = ('serial_no',)

    resource_class = GuideResource
    search_fields = ['serial_no', 'emp_id', 'name', 'email', 'vacancy', 'myImage']


class TeamResource(resources.ModelResource):
    class Meta:
        model = Team

        fields = ('id', 'teamID', 'project_name', 'project_domain', 'project_description', 'no_of_members', 'reg_no_1',
                  'student_1_name', 'student_1_email', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_email', 'student_2_no', 'guide', 'guide_email', 'profile_approved', 'guide_approved', 'rs_paper_approved', 'docs_approved', 'ppt_approved', 'review_2_marks', 'review_3_marks', 'communicated', 'accepted', 'payment_done', 'document', 'ppt', 'rs_paper', 'guide_form', 'type', 'student_1_marks', 'student_2_marks')


class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no', 'guide', 'guide_email', 'profile_approved', 'guide_approved', 'rs_paper_approved', 'docs_approved', 'ppt_approved', 'review_2_marks', 'review_3_marks', 'student_1_marks', 'student_2_marks')
    ordering = ('teamID',)
    search_fields = ('teamID', 'reg_no_1', 'reg_no_2',
                     'project_name', 'project_domain', 'student_1_name', 'student_2_name', 'guide', 'guide_email')
    resource_class = TeamResource


class Temp_TeamResource(resources.ModelResource):
    class Meta:
        model = Temp_Team

        fields = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                  'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no', 'reg_no_3', 'student_3_name', 'student_3_no')


class Temp_TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no')
    ordering = ('teamID',)
    search_fields = ('teamID', 'reg_no_1', 'reg_no_2', 'project_name')
    resource_class = Temp_TeamResource


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'is_active', 'is_staff')
        ordering = ['username']


class NewUserAdmin(ImportExportModelAdmin, UserAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'email', 'is_active', 'is_staff')
    ordering = ['username']
    search_fields = ('username', 'email', 'first_name', 'last_name')

    resource_class = UserResource


class CreditResource(resources.ModelResource):
    class Meta:
        model = Credit
        fields = ('name', 'role', 'img')

class CreditAdmin(ImportExportModelAdmin):
    list_display = ('name', 'role')
    ordering = ['name']
    search_fields = ('name', 'role')

    resource_class = CreditResource

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Otp)
admin.site.register(Otp_Two)
admin.site.register(Temp_Team, Temp_TeamAdmin)
admin.site.register(Temp_User)
admin.site.register(Credit, CreditAdmin)
