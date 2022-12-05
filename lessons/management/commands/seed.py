from django.apps import apps
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Seeding initial data...")

        try:
            pass
        except:
            raise CommandError("Unable to seed initial data.")