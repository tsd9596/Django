from sre_parse import State
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import is_valid_path
from .models import Employee
from .forms import EmployeeForm,Contactform,SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(r):
    return render(r,'greapp/base.html')


@login_required
def about(r):
    return render(r,'greapp/about.html')


def contact(r):
    form=Contactform()
    if r.method == "POST":
        form = Contactform(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    return render(r,'greapp/contact.html',{'form':form})        



def crud(r):
    form=EmployeeForm()
    if r.method == "POST":
        form = EmployeeForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    return render(r,'greapp/crud.html',{'form':form})   


def crud_details(r):
    #details = Employee.objects.all()
    #details = Employee.objects.all().values('empid','Name')
    #details = Employee.objects.all().order_by("Salary").reverse()[0:5]
    #details = Employee.objects.filter(Gender__iexact='Male')
    #details = Employee.objects.exclude(Gender__iexact='Male')
    #details = Employee.objects.filter(State__icontains='Maharashtra')
    #details = Employee.objects.exclude(State__iexact='Maharashtra')
    #details = Employee.objects.filter(State__iendswith='h')
    #details = Employee.objects.filter(Age__gte=30)
    #details = Employee.objects.all().order_by("-Age")[0:5]
    #details = Employee.objects.filter(Salary__lte=30000)    
    #details = Employee.objects.filter(empid__in=[2,4,6,8,10])
    #details = Employee.objects.filter(Gender__iexact='Male').order_by('Salary')[0:3]   
    #details = Employee.objects.filter(Age__lt=30).order_by("-Salary")[0:5]
    #details = Employee.objects.filter(State__iexact='Maharashtra').order_by("-Salary")[0:3]   
    #details = Employee.objects.filter(Mobile__istartswith=9)
    #details = Employee.objects.exclude(Email__icontains='gmail')    
    details = Employee.objects.all()
    #details = Employee.objects.all()    
    #details = Employee.objects.all()
    #details = Employee.objects.all()    
    #details = Employee.objects.all()
    #details = Employee.objects.all()    
    #details = Employee.objects.all()
    #details = Employee.objects.all()    
    #details = Employee.objects.all()
    #details = Employee.objects.all()    
    #details = Employee.objects.all()

    return render(r,'greapp/details.html',{'details':details})
    

def signup(r):
    form=SignupForm()
    if r.method=="POST":
        form=SignupForm(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(r,'greapp/signup.html',{'form':form})           



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'greapp/changepass.html',{'form': form})


def logout(r):
    return render(r,'greapp/logout.html')   

def profile(r):
    return render(r,'greapp/profile.html')    