from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.models import User,auth ,Group
from django.http import Http404, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from django.contrib.auth import authenticate,get_user_model
from django.contrib import auth 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserData,Department ,Activity
from .models import Enq_No,Name_of_Project,Project_Enq,Location
from .forms import UserDataForm,UserCreateForm ,DepartmentForm,ActivityForm,EmployeeDataForm ,UserForm,Enq_NoForm ,Name_of_ProjectForm ,Project_EnqForm,LocationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user ,allowed_user
from django.db.models import F ,Q
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from .filters import UserDataFilter




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


@unauthenticated_user
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

@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel(request):
    employee_data = UserData.objects.all()
    total_employee_data = employee_data.count()
    user = User.objects.all()
    total_user = user.count()
    # total_super_user = user.is_superuser.count()
    last_five = UserData.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    return render(request,'Admin_panel/inbox.htm',{"employee_data":employee_data,'total_user':total_user,'total_employee_data':total_employee_data,'last_five':last_five})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Reg(request):    
    Employee_list = User.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(Employee_list,10)
    try:
        Employee = paginator.page(page)
    except PageNotAnInteger:
        Employee=paginator.page(1)
    except EmptyPage:
        Employee = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/Employee_registrion.htm',{'Employee':Employee})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_User_Add(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Employee')
            user.groups.add(group)
            messages.success(request,'User is created successfully',+username)
            return redirect('User_registrion')

    context = {'form':form}
    return render(request,'Admin_panel/Employee_registrion_Add.htm',context)


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Data(request):
    employee_data = UserData.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(employee_data,1)
    try:
        userdatas = paginator.page(page)
    except PageNotAnInteger:
        userdatas=paginator.page(1)
    except EmptyPage:
        userdatas = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/Employee_data.htm',{"userdatas":userdatas})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_reg_search(request):
    search = request.GET['search']
    Employee = User.objects.filter(username__icontains=search)
    return render(request,'Admin_panel/Employee_registrion.htm',{"Employee":Employee})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_user_update_data(request,pk_id):
    Employee = get_object_or_404(User,id=pk_id)
    form = UserForm(request.POST or None, instance=Employee)
    if form.is_valid():
        form.save()
        return redirect('User_registrion')
    return render(request,'Admin_panel/update_user.htm',{'form':form})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_user_delete_data(request, pk):
    Employee = get_object_or_404(User,id=pk)
    if request.method == "POST":
        Employee.delete()
        return redirect('User_registrion')
    return render(request,'Admin_panel/employee_reg_delete.htm' , {"Employee":Employee})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_data_search(request):
    search = request.GET['search']
    employee_data = UserData.objects.filter(activity__activity=search)
    return render(request,'Admin_panel/Employee_data.htm',{"employee_data":employee_data})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Activity(request):
    activity_list = Activity.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(activity_list,10)
    try:
        activity = paginator.page(page)
    except PageNotAnInteger:
        activity=paginator.page(1)
    except EmptyPage:
        activity = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/activity.htm',{"activity":activity})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Activity_Add(request):
    if request.method == "POST":
        activity_form = ActivityForm(data = request.POST)
        if activity_form.is_valid():
            activity=activity_form.save(commit=False)
            activity.save()
            return redirect('Admin_panel_Activity')
        activity_form = ActivityForm()
        return render(request,'Admin_panel/activity_Add.htm',{'form':activity_form})
    else:
        activity_form = ActivityForm()
        return render(request,'Admin_panel/activity_Add.htm',{'form':activity_form})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Activity_search(request):
    search = request.GET['search']
    activity = Activity.objects.filter(Q(activity__icontains=search))
    return render(request,'Admin_panel/activity.htm',{"activity":activity})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Activity_Delete(request,pk):
    activity = get_object_or_404(Activity,id=pk)
    if request.method == "POST":
        activity.delete()
        return redirect('Admin_panel_Activity')
    return render(request,'Admin_panel/activity_delete.htm' , {"activity":activity})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Activity_Update(request,pk_id):
    activity = get_object_or_404(Activity,id=pk_id)
    form = ActivityForm(request.POST or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_Activity')
    return render(request,'Admin_panel/activity_update.htm',{'form':form})


  


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_deprtmnt(request):
    deprmnt_list = Department.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(deprmnt_list,10)
    try:
        deprmnt = paginator.page(page)
    except PageNotAnInteger:
        deprmnt=paginator.page(1)
    except EmptyPage:
        deprmnt = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/deprtmnt.htm',{"deprmnt":deprmnt})


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_deprtmnt_Add(request):
    department = request.POST["department"]
    deprtmnt_Add = Department(department=department)
    deprtmnt_Add.save()
    return redirect('Admin_panel_deprtmnt')


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_deprtmnt_Update(request,pk_id):
    deprmnt = get_object_or_404(Department,id=pk_id)
    form = DepartmentForm(request.POST or None, instance=deprmnt)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_deprtmnt')
    return render(request,'Admin_panel/deprtmnt_update.htm',{'form':form})
    



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])    
def Admin_panel_deprtmnt_search(request):
    search = request.GET['search']
    deprmnt =Department.objects.filter(department__icontains=search)
    return render(request,'Admin_panel/deprtmnt.htm',{"deprmnt":deprmnt})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_deprtmnt_Delete(request,pk):
    deprmnt = get_object_or_404(Department,id=pk)
    if request.method == "POST":
        deprmnt.delete()
        return redirect('Admin_panel_deprtmnt')
    return render(request,'Admin_panel/deprtmnt_delete.htm' , {"deprmnt":deprmnt})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_enquiry_no(request):
    enquiry_no_list = Enq_No.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(enquiry_no_list,10)
    try:
        enquiry_no = paginator.page(page)
    except PageNotAnInteger:
        enquiry_no=paginator.page(1)
    except EmptyPage:
        enquiry_no = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/enquiry_no.htm',{"enquiry_no":enquiry_no})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_enquiry_no_Search(request):
    search = request.GET['search']
    enquiry_no =Enq_No.objects.filter(enq_no__icontains=search)
    return render(request,'Admin_panel/enquiry_no.htm',{"enquiry_no":enquiry_no})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_enquiry_no_Update(request,pk_id):
    enquiry_no = get_object_or_404(Enq_No,id=pk_id)
    form = Enq_NoForm(request.POST or None, instance=enquiry_no)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_enquiry_no')
    return render(request,'Admin_panel/enquiry_no_update.htm',{'form':form})
    



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_enquiry_no_Delete(request,pk):
    enquiry_no = get_object_or_404(Enq_No,id=pk)
    if request.method == "POST":
        enquiry_no.delete()
        return redirect('Admin_panel_enquiry_no')
    return render(request,'Admin_panel/enquiry_no_delete.htm' , {"enquiry_no":enquiry_no})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_enquiry_no_Add(request):
    if request.method == "POST":
        enquiry_no_form = Enq_NoForm(data = request.POST)
        if enquiry_no_form.is_valid():
            enquiry_no=enquiry_no_form.save(commit=False)
            enquiry_no.save()
            return redirect('Admin_panel_enquiry_no')
        enquiry_no_form = Enq_NoForm()
        return render(request,'Admin_panel/enquiry_no_Add.htm',{'form':enquiry_no_form})
    else:
        enquiry_no_form = Enq_NoForm()
        return render(request,'Admin_panel/enquiry_no_Add.htm',{'form':enquiry_no_form})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_loction(request):
    loction_list = Location.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(loction_list,5)
    try:
        loction = paginator.page(page)
    except PageNotAnInteger:
        loction=paginator.page(1)
    except EmptyPage:
        loction = paginator.page(paginator.num_pages) 
    return render(request,'Admin_panel/loction.htm',{"loction":loction})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_loction_Add(request):
    location = request.POST["location"]
    location_Add = Location(location=location)
    location_Add.save()
    return redirect('Admin_panel_loction')


@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_loction_search(request):
    search = request.GET['search']
    loction = Location.objects.filter(Q(location__icontains=search))
    return render(request,'Admin_panel/loction.htm',{"loction":loction})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_loction_Delete(request,pk):
    loction = get_object_or_404(Location,id=pk)
    if request.method == "POST":
        loction.delete()
        return redirect('Admin_panel_loction')
    return render(request,'Admin_panel/loction_delete.htm' , {"loction":loction})
    



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_loction_Update(request,pk_id):
    loction = get_object_or_404(Location,id=pk_id)
    form = LocationForm(request.POST or None, instance=loction)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_loction')
    return render(request,'Admin_panel/loction_update.htm',{'form':form})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_project_enq(request):
    project_enq_list = Project_Enq.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(project_enq_list,10)
    try:
        project_enq = paginator.page(page)
    except PageNotAnInteger:
        project_enq=paginator.page(1)
    except EmptyPage:
        project_enq = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/projct_enq.htm',{"project_enq":project_enq})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_project_enq_Search(request):
    search = request.GET['search']
    project_enq = Project_Enq.objects.filter(projectEnq__icontains=search)
    return render(request,'Admin_panel/projct_enq.htm',{"project_enq":project_enq})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_project_enq_Update(request,pk_id):
    projct_enq = get_object_or_404(Project_Enq,id=pk_id)
    form = Project_EnqForm(request.POST or None, instance=projct_enq)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_project_enq')
    return render(request,'Admin_panel/projct_enq_update.htm',{'form':form})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_project_enq_Delete(request,pk):
    project_enq = get_object_or_404(Project_Enq,id=pk)
    if request.method == "POST":
        project_enq.delete()
        return redirect('Admin_panel_project_enq')
    return render(request,'Admin_panel/project_enq_delete.htm' ,{"project_enq":project_enq})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_project_enq_Add(request):
    projectEnq = request.POST["projectEnq"]
    projectEnq_Add = Project_Enq(projectEnq=projectEnq)
    projectEnq_Add.save()
    return redirect('Admin_panel_project_enq')

def Admin_panel_name_of_project(request):
    name_of_project_list = Name_of_Project.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(name_of_project_list,10)
    try:
        name_of_project = paginator.page(page)
    except PageNotAnInteger:
        name_of_project=paginator.page(1)
    except EmptyPage:
        name_of_project = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/name_of_project.htm',{"name_of_project":name_of_project})

def Admin_panel_name_of_project_Add(request):
    if request.method == "POST":
        name_of_project_form = Name_of_ProjectForm(data = request.POST)
        if name_of_project_form.is_valid():
            name_of_project = name_of_project_form.save(commit=False)
            name_of_project.save()
            return redirect('Admin_panel_name_of_project')
        name_of_project_form = Name_of_ProjectForm()
        return render(request,'Admin_panel/name_of_project_Add.htm',{'form':name_of_project_form})
    else:
        name_of_project_form = Name_of_ProjectForm()
        return render(request,'Admin_panel/name_of_project_Add.htm',{'form':name_of_project_form})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_name_of_project_Update(request,pk_id):
    name_of_project = get_object_or_404(Name_of_Project,id=pk_id)
    form = Name_of_ProjectForm(request.POST or None, instance=name_of_project)
    if form.is_valid():
        form.save()
        return redirect('Admin_panel_name_of_project')
    return render(request,'Admin_panel/name_of_project_update.htm',{'form':form})



@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_name_of_project_Delete(request,pk):
    name_of_project = get_object_or_404(Name_of_Project,id=pk)
    if request.method == "POST":
        name_of_project.delete()
        return redirect('Admin_panel_name_of_project')
    return render(request,'Admin_panel/name_of_project_delete.htm' ,{"name_of_project":name_of_project})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_name_of_project_Search(request):
    search = request.GET['search']
    name_of_project = Name_of_Project.objects.filter(name_of_project__icontains=search)
    return render(request,'Admin_panel/name_of_project.htm',{"name_of_project":name_of_project})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_employee_data(request):
    employee_data = UserData.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(activity_list,10)
    try:
        activity = paginator.page(page)
    except PageNotAnInteger:
        activity=paginator.page(1)
    except EmptyPage:
        activity = paginator.page(paginator.num_pages)
    return render(request,'Admin_panel/employee_view_data.htm',{"employee_data":employee_data})




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_employee_data_search(request):
    search = request.GET['search']
    employee_data = UserData.objects.filter(activity__activity=search)
    return render(request,'Admin_panel/employee_view_data.htm',{"employee_data":employee_data})





@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Data_update(request,pk_id):
    obj = get_object_or_404(UserData,id=pk_id)
    UserData_form = EmployeeDataForm(request.POST or None,instance=obj)
    if UserData_form.is_valid():
        instance=UserData_form.save(commit=False)
        instance.username = request.user
        instance.save()
        UserData_form.save()
        return redirect('Admin_panel_employee_data')
        messages.success(request,'data has been update successfully  ')
        return redirect('Admin_panel_Data_update')
    return render(request,'Admin_panel/employee_data_Update.htm',{'form':UserData_form})
   




@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_Data_Delete(request,pk):
    Employee = get_object_or_404(UserData,id=pk)
    if request.method == "POST":
        Employee.delete()
        return redirect('Admin_panel_data')
    return render(request,'Admin_panel/Employee_data_delete.htm' , {"Employee":Employee})





@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_employee_data_Add(request):
    if request.method == "POST":
        UserData_form = EmployeeDataForm(data = request.POST)
        if UserData_form.is_valid():
            UserData = UserData_form.save(commit=False)
            UserData.save()
            return redirect('Admin_panel_employee_data')
        UserData_form = EmployeeDataForm()
        return render(request,'Admin_panel/employee_data_Add.htm',{'form':UserData_form})
    else:
        UserData_form = EmployeeDataForm()
        return render(request,'Admin_panel/employee_data_Add.htm',{'form':UserData_form})






@login_required(login_url="login")
@allowed_user(allowed_roles=['Admin'])
def Admin_panel_export_excel_search(request):
    user_list = UserData.objects.all()
    user_filter = UserDataFilter(request.GET, queryset=user_list)
    return render(request, 'Admin_panel/export_excel.htm', {'form': user_filter})