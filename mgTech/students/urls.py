from django.urls import path
from . import views, HodViews, StaffViews, StudentViews

urlpatterns = [
	# Admin Url Path
	path('demo/', views.home, name="Home"),
	path('', views.loginpage, name="LoginPage"),
	path('dologin', views.dologin, name="DoLogin"),
	path('getuserdetails', views.getuserdetails, name="GetUserDetails"),
	path('logoutuser', views.logoutuser, name="LogoutUser"),
	path('adminhome', HodViews.adminhome, name="AdminHome"),

	path('addstaff', HodViews.addstaff, name="AddStaff"),
	path('addstaffsave', HodViews.addstaffsave, name="AddStaffSave"),
	path('managestaffs', HodViews.managestaffs, name="ManageStaffs"),
	path('editstaff/<str:staff_id>', HodViews.editstaff, name="EditStaff"),
	path('editstaffsave', HodViews.editstaffsave, name="EditStaffSave"),

	path('addcourse', HodViews.addcourse, name="AddCourse"),
	path('addcoursesave', HodViews.addcoursesave, name="AddCourseSave"),
	path('managecourses', HodViews.managecourses, name="ManageCourses"),
	path('editcourse/<str:course_id>', HodViews.editcourse, name="EditCourse"),
	path('editcoursesave', HodViews.editcoursesave, name="EditCourseSave"),

	path('addstudent', HodViews.addstudent, name="AddStudent"),
	path('addstudentsave', HodViews.addstudentsave, name="AddStudentSave"),
	path('managestudents', HodViews.managestudents, name="ManageStudents"),
	path('editstudent/<str:student_id>', HodViews.editstudent, name="EditStudent"),
	path('editstudentsave', HodViews.editstudentsave, name="EditStudentSave"),

	path('addsubject', HodViews.addsubject, name="AddSubject"),
	path('addsubjectsave', HodViews.addsubjectsave, name="AddSubjectSave"),
	path('managesubjects', HodViews.managesubjects, name="ManageSubjects"),
	path('editsubject/<str:subject_id>', HodViews.editsubject, name="EditSubject"),
	path('editsubjectsave', HodViews.editsubjectsave, name="EditSubjectSave"),

	path('addsessionyear', HodViews.addsessionyear, name="AddSessionYear"),
	path('addsessionsave', HodViews.addsessionsave, name="AddSessionSave"),

	# Staff URL Path
	path('staff_home/', StaffViews.staff_home, name="StaffHome"),
	path('staff_take_attendance/', StaffViews.staff_take_attendance, name="StaffTakeAttendance"),
	path('get_students/', StaffViews.get_students, name="GetStudents"),
	path('save_attendance_data/', StaffViews.save_attendance_data, name="SaveAttendanceData"),

	# Student URL Path
	path('student_home/', StudentViews.student_home, name="StudentHome"),
]