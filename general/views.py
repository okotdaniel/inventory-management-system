from django.shortcuts import render,redirect,reverse
from general.models import Report,Electronics,AssignElectronics

from django.views.generic import CreateView, DetailView, UpdateView,ListView

#auth stuff
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 

#decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import unauthenticated_user, allowed_users,admin_decorator


#@allowed_users(allowed_roles=['admin'])

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admins')
    context = {

    }
    return render(request, 'general/login.html')



def logoutPage(request):
    logout(request)
    return redirect('login')



#@login_required(login_url='login')

def register(request):
    createUser = UserCreationForm()
    if request.method == "POST":
        createUser = UserCreationForm(request.POST)
        if createUser.is_valid():
            createUser.save()
            return redirect('login')

    context = {
        'createUser':createUser
    }

    return render(request, 'general/register.html', context)




def admins(request):

    #count the number of eleconics
    num_ewaste = Report.objects.all().count()
    num_dep = AssignElectronics.objects.all().count()
    num_electronics = Electronics.objects.all().count()
    recycled = Report.objects.filter(Status="Recycled")
    num_recycled  = recycled.count()

    #querying tables 
    ReportedElectronics = Report.objects.all()
    AssignedElectronics = AssignElectronics.objects.all()
    AllElectronics = Electronics.objects.all()


    
    context = {
        'num_ewaste': num_ewaste,
        'num_dep': num_dep,
        'num_electronics': num_electronics,
        'num_recycled': num_recycled,
        'AllElectronics':AllElectronics,
        'AssignedElectronics':AssignedElectronics,
        'ReportedElectronics':ReportedElectronics
    }
    return render(request, 'general/admin.html', context)



def users(request):
    reported_stuff = Report.objects.all()
    reported_stuff_count = Report.objects.count()
    context = {
        'reported_stuff': reported_stuff,
        'reported_stuff_count':reported_stuff_count
    }
    return render(request, 'general/users.html', context )


class AssignElectronicsView( CreateView):
    #login_url = ''
    #redirect_field_name = ''

    model = AssignElectronics
    fields = '__all__'
    success_url = '/'
    

class AssignedElectronicsView(ListView):
    model = AssignElectronics
    template_name = 'general/assigned.html'
    context_object_name = 'assignedElectronic'



class AddElectronicView(CreateView):
    model = Electronics
    fields = '__all__'
    success_url = '/'


class IssuesCreateView(CreateView):
    model = Report
    #fields = ['Name', 'Department','Issue','Code']
    fields = '__all__'
    success_url = 'reported'

 
class IssuesListView(ListView):
    model = Report
    template_name = 'general/issues.html'
    context_object_name = 'issuesQuery'

class UserIssuesListView(ListView):
    model = Report
    template_name = 'general/reported.html'
    context_object_name = 'UsersIssuesQuery'
