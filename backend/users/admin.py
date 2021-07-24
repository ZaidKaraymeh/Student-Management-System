from django.contrib import admin
from .models import *
# Register your models here.


from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(AttendanceReport)
admin.site.register(Course)
admin.site.register(Subject)
