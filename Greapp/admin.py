from django.contrib import admin
from .models import Employee,Contact

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empid','Name','Gender','DOB','Age','Mobile','City','Salary','Email','State']

admin.site.register(Employee,EmployeeAdmin)    