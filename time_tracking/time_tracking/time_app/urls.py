from django.urls import path
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
    path('User_registrion/',views.Admin_panel_Reg,name='Admin_panel_Reg'),
    path('employee_data/',views.Admin_panel_Data,name='Admin_panel_data'),
    path('Admin_panel_reg_search/',views.Admin_panel_reg_search,name='Admin_panel_reg_search'),
    path('Admin_panel_user_update_data/<str:pk_id>/',views.Admin_panel_user_delete_data,name='Admin_panel_user_update_data'),
    path('Admin_panel_user_delete_data/<str:pk_id>/',views.Admin_panel_user_delete_data,name='Admin_panel_user_delete_data'),
    path('Admin_panel_data_search/',views.Admin_panel_data_search,name='Admin_panel_data_search'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path("password_reset/done",views.password_reset_done, name="password_reset_done"),


]


