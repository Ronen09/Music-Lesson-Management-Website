from django.core.management.base import BaseCommand, CommandError

from lessons.models import User, Term


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Unseeding initial data...")

        try:
            # We use `filter` instead of `get` so there are no errors if the users don't exist yet.
            User.objects.filter(is_superuser=False).delete()
            Term.objects.all().delete()
        except:
            raise CommandError("Unable to unseed initial data.")

        print("Initial data unseeded.")
