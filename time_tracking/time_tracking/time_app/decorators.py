from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request,*args, **kwargs)

    return wrapper_func



def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            return view_func(request,*args, **kwargs)
        return wrapper_func
    return decorator
