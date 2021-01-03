from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, HttpResponseRedirect


class LoginCheckMiddleware(MiddlewareMixin):

	def process_view(self, request, view_func, view_args, view_kwargs):
		modulename=view_func.__module__
		# print modulename
		user = request.user

		# check the if the user is logged in or not
		if user.is_authenticated:
			if user.user_type == "1":
				if modulename == "students.HodViews":
					pass
				elif modulename == "students.views" or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse("AdminHome"))
			elif user.user_type == "2":
				if modulename == "students.StaffViews":
					pass
				elif modulename == "students.views" or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse("StaffHome"))
			elif user.user_type == "3":
				if modulename == "students.StudentViews":
					pass
				elif modulename == "students.views" or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse("StudentHome"))
			else:
				return HttpResponseRedirect(reverse("LoginPage"))
		else:
			if request.path == reverse("LoginPage") or request.path == reverse("DoLogin"):
				pass
			else:
				return HttpResponseRedirect(reverse("LoginPage"))
