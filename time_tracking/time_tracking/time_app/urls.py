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


]


