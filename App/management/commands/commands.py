from fakegen
 import faker import Faker

from django.core.management.base import BaseCommand

from App.models import User, ActivityPeriods

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		fakegen = Faker()
		_id = ['W012A3CDE', 'W067L3HAK', 'W017Q3FGH', 'W089M4XYZ', 'W034J8PQR']
		for _user_id in _id:
			real_name = fakegen.name()
			tz = fakegen.timezone()
			user = User.objects.get_or_create(user_id=_user_id, real_name=real_name, tz=tz)[0]

			for i in range(5):
				start_time = fakegen.date_time()
				end_time = fakegen.date_time()
				acitvity_periods = ActivityPeriods.objects.get_or_create(user=user, start_time=start_time, end_time=end_time)[0]
		self.stdout.write(self.style.SUCCESS('Records saved successfully.'))