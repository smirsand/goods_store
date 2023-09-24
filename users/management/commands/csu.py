from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='smirsand@mail.ru',
            first_name='Sergey',
            last_name='Smirnov',
            is_staff=True,
            is_superuser=True,
            is_activ=True
        )

        user.set_password('2721896')
        user.save()
