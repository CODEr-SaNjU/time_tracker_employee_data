from django import forms
from .models import Activity,Department,Location,Enq_No,Project_Enq,UserData,Enq_No,Name_of_Project
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','is_staff','is_active','is_superuser']

class DateInput(forms.DateInput):
    input_type = 'date'
    # input_type = 'time'

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['department','location','projectEnq','enq_no','name_of_project','activity','submit_data','start_time','end_time']
        widgets = {
             'submit_data':DateInput(attrs={'type': 'date'}),
        }
       


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['activity'].queryset = Activity.objects.none()
        self.fields['enq_no'].queryset = Enq_No.objects.none()
        self.fields['name_of_project'].queryset = Name_of_Project.objects.none()
        if 'department' in self.data or 'projectEnq' in self.data or 'enq_no' in self.data:
            try:
                department_id = int(self.data.get('department'))
                projectEnq_id = int(self.data.get('projectEnq'))
                enq_no_id = int(self.data.get('enq_no'))
                self.fields['activity'].queryset = Activity.objects.filter(department_id=department_id).order_by('activity')
                self.fields['enq_no'].queryset = Enq_No.objects.filter(projectEnq_id=projectEnq_id).order_by('enq_no')
                self.fields['name_of_project'].queryset = Name_of_Project.objects.filter(enq_no_id=enq_no_id).order_by('name_of_project')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty activity queryset
        elif self.instance.pk:
            self.fields['activity'].queryset = self.instance.department.activity_set.order_by('activity')
            self.fields['enq_no'].queryset = self.instance.projectEnq.enq_no_set.order_by('enq_no')
            self.fields['name_of_project'].queryset = self.instance.enq_no.name_of_project_set.order_by('name_of_project')
        
    def clean(self):
        pass


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department']   





class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['department','activity']



class Enq_NoForm(forms.ModelForm):
    class Meta:
        model = Enq_No
        fields = ['enq_no']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location']


class Project_EnqForm(forms.ModelForm):
    class Meta:
        model = Project_Enq
        fields = ['projectEnq']


class Name_of_ProjectForm(forms.ModelForm):
    class Meta:
        model = Name_of_Project
        fields = ['projectEnq','enq_no','name_of_project']