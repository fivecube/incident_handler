from django.core.management import BaseCommand


class Command(BaseCommand):
	def handle(self, *args, **options):
		from django.contrib.auth.models import User
		from incident_alerting.models import Handler
		user_mohit = User.objects.create_user('mohit', 'mohitchouhan1947@gmail.com', 'mohit@django')
		user_mohit.is_staff = True
		user_mohit.is_superuser = True
		user_mohit.save(update_fields=['is_superuser', 'is_staff'])
		Handler.objects.create(name='Alice')
		Handler.objects.create(name='Bob')
		Handler.objects.create(name='Charlie')
