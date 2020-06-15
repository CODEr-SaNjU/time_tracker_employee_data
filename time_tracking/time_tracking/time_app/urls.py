from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('dashboard/',views.home,name='dashboard'),
    path('', views.login,name='login'),
    path('User_registrion/register/',views.register,name='register'),
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
    path('User_registrion/',views.Admin_panel_Reg,name='User_registrion'),
    path('employee_data/',views.Admin_panel_Data,name='Admin_panel_data'),
    path('Admin_panel_reg_search/',views.Admin_panel_reg_search,name='Admin_panel_reg_search'),
    path('Admin_panel_user_update_data/<str:pk_id>/',views.Admin_panel_user_update_data,name='Admin_panel_user_update_data'),
    path('Admin_panel_user_delete_data/<str:pk>/',views.Admin_panel_user_delete_data,name='Admin_panel_user_delete_data'),
    path('Admin_panel_data_search/',views.Admin_panel_data_search,name='Admin_panel_data_search'),
    path('Admin_panel/Activity/',views.Admin_panel_Activity,name='Admin_panel_Activity'),
    path('Admin_panel/deprtmnt/',views.Admin_panel_deprtmnt,name='Admin_panel_deprtmnt'),
    path('Admin_panel/enquiry_no/',views.Admin_panel_enquiry_no,name='Admin_panel_enquiry_no'),
    path('Admin_panel/location/',views.Admin_panel_loction,name='Admin_panel_loction'),
    path('Admin_panel/name_of_project/',views.Admin_panel_name_of_project,name='Admin_panel_name_of_project'),
    path('Admin_panel/project_enquiry/',views.Admin_panel_project_enq,name='Admin_panel_project_enq'),
    path('Admin_panel/employee_data/',views.Admin_panel_employee_data,name='Admin_panel_employee_data'),
    path('forget_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.htm',subject_template_name='registration/password_reset_subject.txt',email_template_name='registration/password_reset_email.html'),name='forget_password'),
    path("password_reset/done",auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

]


