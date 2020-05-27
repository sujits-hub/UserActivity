from django.db import models
from django.utils import timezone

class User(models.Model):
	'''
	This Model is used to store information about the user.
			
	attributes:	
		user_id: unique CharField() which contains the id of the user
		real_name: CharField() which contains the name of the user
		tz: DateTimeField() which contains the timezone
	'''

	user_id = models.CharField(max_length=30)
	real_name = models.CharField(max_length=30)
	tz = models.CharField(max_length=30)

	def __str__(self):
		return self.user_id

class ActivityPeriods(models.Model):
	'''
	This Model is used to store the session of the user that is activity periods of the user.
	
	attributes:
		user: ForeignKey attribute that contains User information
		start_time: DateTimeField() which contains the start_time of the activity of the user
		end_time: DateTimeField() which contains the end_time of the activity of the user
	'''

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.DateTimeField(default=timezone.now())
	end_time = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.user.real_name
