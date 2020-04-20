from django.contrib.auth.models import User
from django.db import models



class Department(models.Model):
    department = models.CharField(max_length=200, verbose_name='Department')
    
    def __str__(self):
        return self.department


class Activity(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200,verbose_name='Activity')

    def __str__(self):
        return self.activity
    
class Location(models.Model):
    location = models.CharField(max_length=100,verbose_name='location')

    def __str__(self):
        return self.location
    

class Project_Enq(models.Model):
    projectEnq = models.CharField(max_length=100,verbose_name="Project_Enq")

    def __str__(self):
        return self.projectEnq
    

class Enq_No(models.Model):
    projectEnq = models.ForeignKey(Project_Enq, on_delete=models.CASCADE)
    enq_no = models.CharField(verbose_name='Enq_No',max_length=20)

    def __str__(self):
        return self.enq_no

class Name_of_Project(models.Model):
    projectEnq = models.ForeignKey(Project_Enq, on_delete=models.CASCADE)
    enq_no = models.ForeignKey(Enq_No, on_delete=models.CASCADE)
    name_of_project = models.CharField(verbose_name="Project_Name",max_length=100)


    def __str__(self):
        return self.name_of_project
    


    

class UserData(models.Model):
    username = models.ForeignKey(User, verbose_name='Employeeid', on_delete=models.CASCADE )
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=False )
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,null=False )
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=False )
    projectEnq = models.ForeignKey(Project_Enq, on_delete=models.CASCADE,null=False )
    enq_no = models.ForeignKey(Enq_No, on_delete=models.CASCADE,null=False )
    name_of_project = models.ForeignKey(Name_of_Project, on_delete=models.CASCADE,null=False )
    start_time = models.TimeField(verbose_name="Starting Time",auto_now=False, auto_now_add=False)
    end_time = models.TimeField(verbose_name="Ending Time", auto_now=False,  auto_now_add=False)
    submit_data = models.DateField(verbose_name='Submit Date',auto_now_add=False)
    hours = models.DurationField("Hours",blank=True,null=True)
    


