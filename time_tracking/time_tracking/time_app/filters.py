import django_filters

from .models import *

class UserDataFilter(django_filters.FilterSet):
    class Meta:
        model = UserData
        fileds = ['submit_data','enq_no']