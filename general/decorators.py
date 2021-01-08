from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')          
        else:
            return view_func(request, *args, **kwargs)
            
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

'''
def admin_decorator(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'users':
            return redirect('users')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
 '''      

def admin_decorator(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'users':
            return redirect('users')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function

"""
If the decorator is expecting parameters, those parameters will be represented at the top of the nest,
Decorator has the class-based view while the wrapper function has the parameters of the class-based view
"""

'''
def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            role = None
            if request.user.role:
                role = request.user.role
            if role in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')

        return wrapper_function

    return decorator


count = 0
old_users_name = ""

def admin_redirect(view_func):

    def wrapper_func(request, *args, **kwargs):
        global old_users_name
        global count
        current_users_name = request.user.first_name + request.user.last_name

        if old_users_name != current_users_name: #Someone new has logged in
            count = 0
            old_users_name = current_users_name


        print("Inside admin redirect")
        if count == 0:
            if request.user.is_staff:
                count = count + 1 #Used to ensure that once a user has logged in and accessed the adminDashboard they
                                  #can still make an application for leave
                return redirect('adminDashboard:pending')
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)


    return wrapper_func

'''