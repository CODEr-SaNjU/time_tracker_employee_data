from django.contrib import admin
from .forms import UserDataForm
from django.contrib.auth.models import Group
from . models import Location,Department,Project_Enq,Activity,Name_of_Project,Enq_No
from time_app.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin





class UserDataAdmin(admin.ModelAdmin):
    list_display = ('department','username','location','projectEnq','enq_no','name_of_project','activity','submit_data','start_time','end_time','hours')
    list_filter = ('department','location','projectEnq','enq_no','name_of_project',)


    
















admin.site.register(UserData,UserDataAdmin)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Enq_No)
admin.site.register(Activity)
admin.site.register(Name_of_Project)
admin.site.register(Project_Enq)
admin.site.unregister(Group)
