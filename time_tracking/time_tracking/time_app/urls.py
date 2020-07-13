from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('dashboard/',views.home,name='dashboard'),
    path('', views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path("userdata_create_new/",views.userdata_create_new, name="userdata_create_new"),
    path('load-activity/', views.load_activity, name='ajax_load_activity'),
    path('load-enq-no/', views.load__enq_no, name='ajax_load_enq_no'),
    path('load_name_of_project/', views.load_name_of_project, name='ajax_load_name_of_project'),
    path("user_update_data/<str:pk_id>/",views.user_update_data, name="user_update_data"),
    path("change_password/",views.user_change_password, name="user_change_password"),
    path("user_data_filter/",views.user_data_filter,name="user_data_filter"),
    path('user_time/',views.user_time,name="user_time"),
    path('submitted_data/',views.submitted_data,name='submitted_data'),
    path('Admin_panel/',views.Admin_panel,name='Admin_panel'),


    path('Admin_panel/User/',views.Admin_panel_Reg,name='User_registrion'),
    path('Admin_panel/User/Add/',views.Admin_panel_User_Add,name='Admin_panel_User_Add'),
    path('Admin_panel/User/search/',views.Admin_panel_reg_search,name='Admin_panel_reg_search'),
    path('Admin_panel/user/Update/<str:pk_id>/',views.Admin_panel_user_update_data,name='Admin_panel_user_update_data'),
    path('Admin_panel/user/Delete/<str:pk>/',views.Admin_panel_user_delete_data,name='Admin_panel_user_delete_data'),

    path('Admin_panel/employee_data/',views.Admin_panel_Data,name='Admin_panel_data'),
    path('Admin_panel/employee_data/Update/<str:pk_id>',views.Admin_panel_Data_update,name='Admin_panel_Data_update'),
    path('Admin_panel/employee_data/Delete/<str:pk>/',views.Admin_panel_Data_Delete,name='Admin_panel_Data_Delete'),
 





    path('Admin_panel/employee_data/search/',views.Admin_panel_data_search,name='Admin_panel_data_search'),
    
    path('Admin_panel/employee_data/Activity/',views.Admin_panel_Activity,name='Admin_panel_Activity'),
    path('Admin_panel/employee_data/Activity/Delete/<str:pk>/',views.Admin_panel_Activity_Delete,name='Admin_panel_Activity_Delete'),
    path('Admin_panel/employee_data/Activity/Update/<str:pk_id>/',views.Admin_panel_Activity_Update,name='Admin_panel_Activity_Update'),
    path('Admin_panel/employee_data/Activity/Activity_search/',views.Admin_panel_Activity_search,name='Admin_panel_Activity_search'),


    path('Admin_panel/employee_data/deprtmnt/Search/',views.Admin_panel_deprtmnt_search,name='Admin_panel_deprtmnt_search'),
    path('Admin_panel/employee_data/deprtmnt/',views.Admin_panel_deprtmnt,name='Admin_panel_deprtmnt'),
    path('Admin_panel/employee_data/deprtmnt/Update/<str:pk_id>/',views.Admin_panel_deprtmnt_Update,name='Admin_panel_deprtmnt_Update'),
    path('Admin_panel/employee_data/deprtmnt/Delete/<str:pk>/',views.Admin_panel_deprtmnt_Delete,name='Admin_panel_deprtmnt_Delete'),
    path('Admin_panel/employee_data/deprtmnt/Add/',views.Admin_panel_deprtmnt_Add,name='Admin_panel_deprtmnt_Add'),

    
    path('Admin_panel/employee_data/enquiry_no/',views.Admin_panel_enquiry_no,name='Admin_panel_enquiry_no'),
    path('Admin_panel/employee_data/enquiry_no/Add/',views.Admin_panel_enquiry_no_Add,name='Admin_panel_enquiry_no_Add'),
    path('Admin_panel/employee_data/enquiry_no/Update/<str:pk_id>/',views.Admin_panel_enquiry_no_Update,name='Admin_panel_enquiry_no_Update'),
    path('Admin_panel/employee_data/enquiry_no/Delete/<str:pk>/',views.Admin_panel_enquiry_no_Delete,name='Admin_panel_enquiry_no_Delete'),
    path('Admin_panel/employee_data/enquiry_no/Search/',views.Admin_panel_enquiry_no_Search,name='Admin_panel_enquiry_no_Search'),




    path('Admin_panel/employee_data/loction/Add/',views.Admin_panel_loction_Add,name='Admin_panel_loction_Add'),
    path('Admin_panel/employee_data/location/',views.Admin_panel_loction,name='Admin_panel_loction'),
    path('Admin_panel/employee_data/location/Search/',views.Admin_panel_loction_search,name='Admin_panel_loction_search'),
    path('Admin_panel/employee_data/location/Delete/<str:pk>/',views.Admin_panel_loction_Delete,name='Admin_panel_loction_Delete'),
    path('Admin_panel/employee_data/location/Update/<str:pk_id>/',views.Admin_panel_loction_Update,name='Admin_panel_loction_Update'),


    path('Admin_panel/employee_data/name_of_project/',views.Admin_panel_name_of_project,name='Admin_panel_name_of_project'),
    path('Admin_panel/employee_data/name_of_project/Add/',views.Admin_panel_name_of_project_Add,name='Admin_panel_name_of_project_Add'),
    path('Admin_panel/employee_data/name_of_project/Delete/<str:pk>/',views.Admin_panel_name_of_project_Delete,name='Admin_panel_name_of_project_Delete'),
    path('Admin_panel/employee_data/name_of_project/Update/<str:pk_id>/',views.Admin_panel_name_of_project_Update,name='Admin_panel_name_of_project_Update'),
    path('Admin_panel/employee_data/name_of_project/Search/',views.Admin_panel_name_of_project_Search,name='Admin_panel_name_of_project_Search'),


    path('Admin_panel/employee_data/project_enquiry/',views.Admin_panel_project_enq,name='Admin_panel_project_enq'),
    path('Admin_panel/employee_data/project_enquiry/Search/',views.Admin_panel_project_enq_Search,name='Admin_panel_project_enq_Search'),
    path('Admin_panel/employee_data/project_enquiry/Update/<str:pk_id>/',views.Admin_panel_project_enq_Update,name='Admin_panel_project_enq_Update'),
    path('Admin_panel/employee_data/project_enquiry/Delete/<str:pk>/',views.Admin_panel_project_enq_Delete,name='Admin_panel_project_enq_Delete'),
    path('Admin_panel/employee_data/project_enq/Add/',views.Admin_panel_project_enq_Add,name='Admin_panel_project_enq_Add'),


    path('Admin_panel/employee_data/employee_data/',views.Admin_panel_employee_data,name='Admin_panel_employee_data'),
    path('Admin_panel/employee_data/employee_data/search/',views.Admin_panel_employee_data_search,name='Admin_panel_employee_data_search'),
    path('forget_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.htm',subject_template_name='registration/password_reset_subject.txt',email_template_name='registration/password_reset_email.html'),name='forget_password'),
    path("password_reset/done",auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

]


