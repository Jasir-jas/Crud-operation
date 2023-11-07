from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    empList = {'employee_list' : Employee.objects.all()}
    return render(request,'employee_list.html',empList)

def employee_form(request,pk=0):
    if request.method  == "GET":
        if pk==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=pk)
            form = EmployeeForm(instance = employee)
        return render(request,'employee_form.html',{'form' : form})

    else:
        if pk == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=pk)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/list')



def employee_delete(request,pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('/list')

