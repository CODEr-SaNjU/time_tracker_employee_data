import django_filters

from .models import *
from django.contrib.auth.models import User


class UserDataFilter(django_filters.FilterSet):
    class Meta:
        model = UserData
        fields = ['username', 'department', ]