from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from App.models import User, ActivityPeriods
from datetime import datetime

class GetMetricsView(View):

	def time_in_format(self, time):
		return time.strftime("%b %d %Y %I:%M%p")

	def get(self, request):
		result = {}
		members = []
		result["ok"] = False
		for entry in User.objects.all():

			user = {}
			activity_periods = []

			user["id"] = entry.user_id
			user["real_name"] = entry.real_name
			user["tz"] = entry.tz

			activity = ActivityPeriods.objects.filter(user=entry)

			for entries in activity:
				element = {}
				element["start_time"] = self.time_in_format(entries.start_time)
				element["end_time"] = self.time_in_format(entries.end_time)
				activity_periods.append(element)

			user["activity_periods"] = activity_periods
			members.append(user)

		result["members"] = members
		result["ok"] = True

		return JsonResponse(result)

class UserListView(View):

	template_name = 'user_list.html'

	def get(self, request):
		form = {}
		user_list = []
		for user in User.objects.all():
			user_list.append(user.user_id)
		form["user_list"] = user_list
		return render(request, self.template_name, {'form': form})

class UserDetailView(View):

	template_name = 'user_detail.html'

	def time_in_format(self, time):
		return time.strftime("%b %d %Y %I:%M%p")

	def get(self, request, user_id):
		form = {}
		_user = User.objects.filter(user_id=user_id)
		user = _user[0]
		form["user_id"] = user.user_id
		form["real_name"] = user.real_name
		form["tz"] = user.tz

		acitvity = ActivityPeriods.objects.filter(user=user)

		activity_periods = []
		for entries in acitvity:
			element = {}
			element["start_time"] = self.time_in_format(entries.start_time)
			element["end_time"] = self.time_in_format(entries.end_time)
			activity_periods.append(element)
		form["activity_periods"] = activity_periods

		return render(request, self.template_name, {'form':form})

class IndexView(View):

	template_name = 'index.html'

	def get(self, request):
		return render(request, self.template_name)