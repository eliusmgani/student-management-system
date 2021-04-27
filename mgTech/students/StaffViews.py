from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


def staff_home(request):
	return render(request, "staff_templates/staff_home_content.html")

def staff_take_attendance(request):
	subjects = Subjects.objects.filter(staff_id=request.user.id)
	session_years = SessionYearModel.objects.all()
	context = {
		'subjects': subjects,
		'session_years': session_years,
	}
	return render(request, "staff_templates/staff_take_attendance.html", context)

# WE don't need csrf_token when using Ajax
@csrf_exempt
def get_students(request):
	# Getting Values from Ajax POST "Fetch Student"
	subject_id = request.POST.get("subject")
	session_year = request.POST.get("session_year")

	# Students enroll to Course, Course has Subjects
	# Getting all Data from Subject Model based on subject_id
	subject_model = Subjects.objects.get(id=subject_id)
	session_model = SessionYearModel.objects.get(id=session_year)
	students = Students.objects.filter(course_id=subject_model.course_id, session_year_id=session_model)
	
	# Only Passing Student Id and Student Name Only
	list_data = []
	for student in students:
		data_small = {
			"id": student.admin.id,
			"name": student.admin.first_name+" "+student.admin.last_name,
			}
		list_data.append(data_small)
	return JsonResponse(json_dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def save_attendance_data(request):
	# Get Values from Staff Take Attendance Form via Ajax (JavaScript)
	# Use Getlist to Access HTML Array/List Input Data
	student_ids = request.POST.get("student_ids")
	subject_id = request.POST.get("subject_id")
	attendance_date = request.POST.get("attendance_date")
	session_year_id = request.POST.get("session_year_id")

	subject_model = Subjects.objects.get(id=subject_id)
	session_model = SessionYearModel.objects.get(id=session_year_id)
	json_student = json.loads(student_ids)
	#print(data[0]['id'])

	try:
		# First Attendance Data is Saved on Attendance Model
		attendance=Attendance(subject_id=subject_model, attendance_date=attendance_date, session_year_id=session_model)
		attendance.save()

		for stud in json_student:
			# Attendance of Individual Student saved on AttendanceReport Model
			student = Students.objects.get(admin=stud['id'])
			attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
			attendance_report.save()
		return HttpResponse("Succeed")
	except:
		return HttpResponse("Internal Error")