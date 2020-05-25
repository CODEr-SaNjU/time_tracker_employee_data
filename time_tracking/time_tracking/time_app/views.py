from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.models import User,auth
from django.http import Http404, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from django.contrib.auth import authenticate,get_user_model
from django.contrib import auth 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserData,Department ,Activity
from .models import Enq_No,Name_of_Project,Project_Enq
from .forms import UserDataForm
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user ,allowed_user
from django.db.models import F
import datetime
import xlwt

@unauthenticated_user
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Error! please enter the correct Employee Username and Password for a staff account.')
            return render(request,'html_files/login.htm')

    else:
        return render(request,'html_files/login.htm')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return render(request,'html_files/logout.htm')
       

@login_required(login_url='login')
def home(request):
    return render(request,'html_files/Main.htm')


# @unauthenticated_user
def register(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        Employeeid = request.POST['empid']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=Employeeid).exists():
                messages.info(request,'employee id already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return  redirect('register')
            # elif not Employeeid.isupper():
            #     messages.info(request,"Employeeid should be  uppercase")
            #     return redirect('register')
            # elif not 'MOBTR' in Employeeid:
            #     messages.info(request,"Employeeid should be in correct")
            #     return redirect('register')
            # elif not 'geodesictechniques' in email:
            #     messages.info(request,"email should be in correct format")
            #     return redirect('register')
            # elif 'gmail' in email:
            #     messages.info(request,"email should be in correct format")
            #     return redirect('register')
            else:
                user = User.objects.create_user(email=email,username=Employeeid,password=password,first_name=name)
                user.save()
                messages.success(request,'registration has been successfully completed '+name)
                return redirect('register')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'html_files/register.htm')

         
@login_required(login_url='login')   
def userdata_create_new(request):
    if request.method == "POST":
        userdata_form = UserDataForm(data = request.POST)
        if userdata_form.is_valid():
            Employee=userdata_form.save(commit=False)
            Employee.username = request.user
            Employee.save()
            return redirect('user_time')
        userdata_form = UserDataForm()
        return render(request,'html_files/user_form.htm',{'form':userdata_form})
    else:
        userdata_form = UserDataForm()
        return render(request,'html_files/user_form.htm',{'form':userdata_form})

@login_required(login_url='login')
def load_activity(request):
    department_id = request.GET.get('department')
    activites = Activity.objects.filter(department_id=department_id).order_by('activity')
    return render(request, 'html_files/activity_dropdown.htm',{'activites': activites})

@login_required(login_url='login')
def load__enq_no(request):
    projectEnq_id = request.GET.get('projectEnq')
    enq_nos = Enq_No.objects.filter(projectEnq_id=projectEnq_id).order_by('enq_no')
    return render(request, 'html_files/enq_no_dropdown.htm',{'enq_nos': enq_nos})

@login_required(login_url='login')
def load_name_of_project(request):
    enq_no_id = request.GET.get('enq_no')
    nameofprojects = Name_of_Project.objects.filter(enq_no_id=enq_no_id).order_by('name_of_project')
    return render(request, 'html_files/name_of_project.htm',{'nameofprojects': nameofprojects})

@login_required(login_url='login')
def user_update_data(request,pk_id):
    obj = get_object_or_404(UserData,id=pk_id)
    form = UserDataForm(request.POST or None,instance=obj)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.username = request.user
        instance.save()
        form.save()
        return redirect('user_time')
        messages.success(request,'data has been update successfully  ')
        return redirect('user_update_data')
    return render(request,'html_files/user_update_data.htm',{'form':form})
   

@login_required(login_url='login')
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'html_files/change_password.htm', {
        'form': form
    })

@login_required(login_url='login')
def user_data_filter(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        main_data = date.split(' ')
        for i in range(len(main_data)):
            months = ['January','February','March','April','May','June','July','August','September','October','November','December']
            month = main_data[0]
            month_num = months.index(month)+1
            year = main_data[1]
            userdata = UserData.objects.filter(username=request.user,submit_data__month=month_num,submit_data__year = year).order_by('-submit_data')
            return render(request,'html_files/user_data_filter.htm',{'userdata':userdata})
        return HttpResponse("Not Found")
   


@login_required(login_url='login')
def user_time(request):
    userdata = UserData.objects.update(hours = F('end_time')-F('start_time'))
    return render(request,'html_files/user_data_confirm.htm',{'userdata':userdata})


@login_required(login_url="login")
def submitted_data(request):
    userdata = UserData.objects.filter(username=request.user,submit_data__lte=datetime.datetime.today(),submit_data__gt=datetime.datetime.today()-datetime.timedelta(days=15)).order_by('-submit_data')
    return render(request,'html_files/Home.htm',{'userdata':userdata})


def Admin_panel(request):
    employee_data = UserData.objects.all()
    total_employee_data = employee_data.count()
    user = User.objects.all()
    total_user = user.count()
    # total_super_user = user.is_superuser.count()
    last_five = UserData.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    return render(request,'Admin_panel/inbox.htm',{"employee_data":employee_data,'total_user':total_user,'total_employee_data':total_employee_data,'last_five':last_five})


def Admin_panel_Reg(request):
    Employee = User.objects.all()
    return render(request,'Admin_panel/Employee_registrion.htm',{'Employee':Employee})
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        Employeeid = request.POST['empid']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=Employeeid).exists():
                messages.info(request,'employee id already exists')
                return redirect('register')
            elif User.objects.filter(email=email).eobjectxists():
                messages.info(request,'email already exists')
                return  redirect('Admin_panel_Reg')
            # elif not Employeeid.isupper():
            #     messages.info(request,"Employeeid should be  uppercase")
            #     return redirect('Admin_panel_Reg')
            # elif not 'MOBTR' in Employeeid:
            #     messages.info(request,"Employeeid should be in correct")
            #     return redirect('Admin_panel_Reg')
            # elif not 'geodesictechniques' in email:
            #     messages.info(request,"email should be in correct format")
            #     return redirect('Admin_panel_Reg')
            # elif 'gmail' in email:
            #     messages.info(request,"email should be in correct format")
            #     return redirect('Admin_panel_Reg')
            else:
                user = User.objects.create_user(email=email,username=Employeeid,password=password,first_name=name)
                user.save()
                messages.success(request,'registration has been successfully completed '+name)
                return redirect('Admin_panel_Reg')
        else:
            messages.info(request,'password not matching')
            return redirect('Admin_panel_Reg')
    else:
        return render(request,'Admin_panel/Employee_registrion.htm')

def Admin_panel_Data(request):
    employee_data = UserData.objects.all()
    return render(request,'Admin_panel/Employee_data.htm',{"employee_data":employee_data})

def Admin_panel_reg_search(request):
    search = request.GET['search']
    Employee = User.objects.filter(username__icontains=search)
    return render(request,'Admin_panel/Employee_registrion.htm',{"Employee":Employee})

def Admin_panel_user_update_data(request,pk_id):
    obj = get_object_or_404(User,id=pk_id)                                   
    if form.is_valid():
        instance=form.save(commit=False)
        instance.username = request.user
        instance.save()
        form.save()
        messages.success(request,'data has been update successfully  ')
        return redirect('Admin_panel_user_update_data')
    return render(request,'Admin_panel/edit_user.htm',{'form':form})

def Admin_panel_user_delete_data(request, pk):
    Employee = get_object_or_404(User,id=pk)
    if request.method == "POST":
        Employee.delete()
        return redirect('Admin_panel_Reg')
    return render(request,'Admin_panel/employee_reg_delete.htm' , {"Employee":Employee})
def Admin_panel_data_search(request):
    search = request.GET['search']
    employee_data = UserData.objects.filter(foreinkeyfield__foreinkeyfield__username=search)
    return render(request,'Admin_panel/Employee_data.htm',{"employee_data":employee_data})

