from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from . forms import AddStudentForm, EditStudentForm
from . models import CustomUser, Staffs, Students, Courses, Subjects
from django.core.files.storage import FileSystemStorage #Used for uploading Profile Picture
from django.http import HttpResponse, HttpResponseRedirect

def adminhome(request):
    return render(request, "admin_templates/main.html")


def addstaff(request):
    return render(request, "admin_templates/addstaff.html")

def addstaffsave(request):
    if request.method != "POST":
        messages.error(request, f'Invalid Method..!!')
        return HttpResponseRedirect(reverse("AddStaff"))

    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, f'Staff Added Successfully..!!')
            return HttpResponseRedirect(reverse("AddStaff"))
        except:
            messages.error(request, f'Failed to Add Staff..!!')
            return HttpResponseRedirect(reverse("AddStaff"))

def managestaffs(request):
    staffs = Staffs.objects.all()
    context = {
        'staffs': staffs
    }
    return render(request, "admin_templates/managestaffs.html", context)

def editstaff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    context = {
        'id': staff_id,
        'staff': staff,
    }
    return render(request, "admin_templates/editstaff.html", context)

def editstaffsave(request):
    if request.method != "POST":
        messages.error(request, f'Invalid Method..!!')
        return HttpResponseRedirect(reverse("EditStaff"))
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")

        try:
            # Insert Data into CustomUser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            # Insert Data into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request, f'Staff Edited Successfully..!!')
            return HttpResponseRedirect(reverse("EditStaff", kwargs={"staff_id": staff_id}))
        except:
            messages.error(request, f'Failed to Edit Staff..!!')
            return HttpResponseRedirect(reverse("EditStaff", kwargs={"staff_id": staff_id}))


def addcourse(request):
    return render(request, "admin_templates/addcourse.html")

def addcoursesave(request):
    if request.method != "POST":
        messages.error(request, f'Method is Not Allowed..!!')
        return HttpResponseRedirect(reverse("AddCourse"))
    else:
        course = request.POST.get("course")

        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, f'Course Added Successfully..!!')
            return HttpResponseRedirect(reverse("AddCourse"))
        except:
            messages.error(request, f'Failed To Add Course..!!')
            return HttpResponseRedirect(reverse("AddCourse"))

def managecourses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, "admin_templates/managecourse.html", context)

def editcourse(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        'id': course_id,
        'course': course,
    }
    return render(request, "admin_templates/editcourse.html", context)

def editcoursesave(request):
    if request.method != "POST":
        messages.error(request, f'Invalid Method..!!')
        return HttpResponseRedirect(reverse("EditCourse"))
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request, f'Course Edited Successfully..!!')
            return HttpResponseRedirect(reverse("EditCourse", kwargs={"course_id": course_id}))
        except:
            messages.error(request, f'Failed To Edit Course..!!')
            return HttpResponseRedirect(reverse("EditCourse", kwargs={"course_id": course_id}))

def addstudent(request):
    #courses = Courses.objects.all()
    form = AddStudentForm
    context = {
        'form': form,
        #'courses':courses
    }
    return render(request, "admin_templates/addstudent.html", context)

def addstudentsave(request):
    if request.method != "POST":
        messages.error(request, f'Method is Not Allowed..!!')
        return HttpResponseRedirect(reverse("AddStudent"))
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            session_start_year = form.cleaned_data["start_year"]
            session_end_year = form.cleaned_data["end_year"]

            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            profile_pic=request.FILES["profile_pic"]
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, user_type=3)
                user.students.address = address
                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                user.students.gender = gender
                user.students.session_start_year = session_start_year
                user.students.session_end_year = session_end_year
                user.students.profile_pic=profile_pic_url
                user.save()
                messages.success(request, f'Student Added Successfully..!!')
                return HttpResponseRedirect(reverse("AddStudent"))
            except:
                messages.error(request, f'Failed to Add Student..!!')
                return HttpResponseRedirect(reverse("AddStudent"))
        else:
            form = AddStudentForm()
            context = {'form': form}
            return render(request, "admin_templates/addstudent.html", context)


def managestudents(request):
    students = Students.objects.all()
    context = {
        'students': students,
    }
    return render(request, "admin_templates/managestudents.html", context)

def editstudent(request, student_id):
    # Adding Student ID into Session Variable
    request.session['student_id']=student_id
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()
    form = EditStudentForm()
    # Filling the form with Data from Database
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['email'].initial=student.admin.email
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['gender'].initial=student.gender
    form.fields['session_start_year'].initial=student.session_start_year
    form.fields['session_end_year'].initial=student.session_end_year
    form.fields['profile_pic'].initial=student.profile_pic

    context = {
        'id': student_id,
        'form': form,
        "username": student.admin.username,
    }
    return render(request, "admin_templates/editstudent.html", context)

def editstudentsave(request):
    if request.method != "POST":
        messages.error(request, f'Method is Not Allowed..!!')
        return HttpResponseRedirect(reverse("EditStudent"))
    else:
        student_id = request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("managestudents"))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            session_start_year = form.cleaned_data["session_start_year"]
            session_end_year = form.cleaned_data["session_end_year"]

            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if request.FILES.get("profile_pic", False):
                profile_pic=request.FILES["profile_pic"]
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name, profile_pic)
                profile_pic_url=fs.url(profile_pic)
            else:
                profile_pic_url=None

            try:
                # Insert Student's Data into CustomUser Model
                user = CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                # Inserting Student's Data into Students Model
                student = Students.objects.get(admin=student_id)
                course = Courses.objects.get(id=course_id)
                student.address=address
                student.gender=gender
                student.session_start_year=session_start_year
                student.session_end_year=session_end_year
                student.course_id=course
                if profile_pic_url != None:
                    student.profile_pic=profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request, f'Student Edited Successfully..!!')
                return HttpResponseRedirect(reverse("EditStudent", kwargs={"student_id": student_id}))
            except:
                messages.error(request, f'Failed to Edit Student..!!')
                return HttpResponseRedirect(reverse("EditStudent", kwargs={"student_id": student_id}))
        else:
            form = EditStudentForm()
            student = Students.objects.get(admin=student_id)
            context = {
                'id': student_id,
                'form': form,
                "username": student.admin.username,
                }
            return render(request, "admin_templates/editstudent.html", context)

def addsubject(request):
    staffs = CustomUser.objects.filter(user_type=2)
    courses = Courses.objects.all()
    context = {
        'courses': courses,
        'staffs': staffs
    }
    return render(request, "admin_templates/addsubject.html", context)

def addsubjectsave(request):
    if request.method != "POST":
        messages.error(request, f'Method is Not Allowed..!!')
        return HttpResponseRedirect(reverse("AddSubject"))
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        staff_id = request.POST.get("staff")
        course = Courses.objects.get(id=course_id)
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, f'Subject Added Successfully..!!')
            return HttpResponseRedirect(reverse("AddSubject"))
        except:
            messages.error(request, f'Failed to Add Subject..!!')
            return HttpResponseRedirect(reverse("AddSubject"))

def managesubjects(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, "admin_templates/managesubjects.html", context)

def editsubject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    context = {
        'id': subject_id,
        'subject': subject,
        'courses': courses,
        'staffs': staffs
    }
    return render(request, "admin_templates/editsubject.html", context)

def editsubjectsave(request):
    if request.method != "POST":
        messages.error(request, f'Method is Not Allowed..!!')
        return HttpResponseRedirect(reverse("EditSubject"))
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")
        staff = CustomUser.objects.get(id=staff_id)
        course = Courses.objects.get(id=course_id)

        try:
            subject = Subjects.objetcs.get(id=subject_id)
            subject.subject_name=subject_name
            subject.staff_id=staff_id
            subject.course_id=course_id
            subject.save()
            messages.success(request, f'Subject Edited Successfully..!!')
            return HttpResponseRedirect(reverse("EditSubject", kwargs={"subject_id": subject_id}))
        except:
            messages.error(request, f'Failed To Edit Subject..!!')
            return HttpResponseRedirect(reverse("EditSubject", kwargs={"subject_id": subject_id}))