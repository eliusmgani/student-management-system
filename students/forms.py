from django import forms
from . models import *


class DateInput(forms.DateInput):
	input_type = "date"

class AddStudentForm(forms.Form):
	first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter First Name"}))
	last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter Last Name"}))
	username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter Username"}))
	email = forms.EmailField(label="Email Address", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}))
	password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}))
	address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Address"}))

	gender_choices = {
		("Male", "Male"),
		("Feamale", "Female"),
	}

	course_list = []
	try:
		courses = Courses.objects.all()
		for course in courses:
			small_course = (course.id, course.course_name)
			course_list.append(small_course)
	except:
		course_list = []

	session_list = []
	try:
		sessions = SessionYearModel.objects.all()
		for ses in sessions:
			ses = (ses.id, str(ses.session_start_year)+" -- "+str(ses.session_end_year))
			session_list.append(ses)
	except:
		pass
		#session_list = []

	course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
	gender = forms.ChoiceField(label="Gender", choices=gender_choices, widget=forms.Select(attrs={"class": "form-control"}))
	session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
	#end_year = forms.DateField(label="End Year", widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
	profile_pic = forms.FileField(label="Profile Picture", widget=forms.FileInput(attrs={"class": "form-control"}))


class EditStudentForm(forms.Form):
	first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter First Name"}))
	last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter Last Name"}))
	username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter Username"}))
	email = forms.EmailField(label="Email Address", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}))
	address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Address"}))

	gender_choices = {
		("Male", "Male"),
		("Feamale", "Female"),
	}

	courses = Courses.objects.all()
	course_list = []
	for course in courses:
		small_course = (course.id, course.course_name)
		course_list.append(small_course)

	session_list = []
	try:
		sessions = SessionYearModel.objects.all()
		for ses in sessions:
			ses = (ses.id, str(ses.session_start_year)+" -- "+str(ses.session_end_year))
			session_list.append(ses)
	except:
		pass
		#session_list = []

	course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
	gender = forms.ChoiceField(label="Gender", choices=gender_choices, widget=forms.Select(attrs={"class": "form-control"}))
	session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
	#session_end_year = forms.DateField(label="End Year", widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
	profile_pic = forms.FileField(label="Profile Picture", widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
