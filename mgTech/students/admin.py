from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Students, Courses, Subjects, Attendance, StudentsAttendanceReport, StudentsLeaveReport, StaffsLeaveReport, StudentsFeedBack, StaffsFeedBack, StudentsNotification, StaffsNotification, StudentResults, SessionYearModel


# Register your models here.

class UserModel(UserAdmin):
	pass

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Attendance)
admin.site.register(StudentsAttendanceReport)
admin.site.register(StudentsLeaveReport)
admin.site.register(StaffsLeaveReport)
admin.site.register(StudentsFeedBack)
admin.site.register(StaffsFeedBack)
admin.site.register(StudentsNotification)
admin.site.register(StaffsNotification)
admin.site.register(StudentResults)
admin.site.register(SessionYearModel)
