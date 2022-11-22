from django.core.management.base import BaseCommand, CommandError

from lessons.models.user import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Seeding initial data...")
        try:
            if len(User.objects.filter(email="john.doe@example.org")) == 0:
                User.objects.create_user(
                    "john.doe@example.org",
                    "Password123",
                    first_name="John",
                    last_name="Doe",
                    role="Student",
                )

            if len(User.objects.filter(email="petra.pickles@example.org")) == 0:
                User.objects.create_user(
                    "petra.pickles@example.org",
                    "Password123",
                    first_name="Petra",
                    last_name="Pickles",
                    role="Administrator",
                )

            if len(User.objects.filter(email="marty.major@example.org")) == 0:
                User.objects.create_user(
                    "marty.major@example.org",
                    "Password123",
                    first_name="Marty",
                    last_name="Major",
                    role="Director",
                )

            print("Data was seeded.")
        except:
            raise CommandError("Unable to seed data.")
