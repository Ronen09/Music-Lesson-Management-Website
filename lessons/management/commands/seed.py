from django.core.management.base import BaseCommand, CommandError

from lessons.models import User, Term

from datetime import datetime


class Command(BaseCommand):

    def add_users(self):
        users = [{
            "email": "john.doe@example.org",
            "password": "Password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Student",
        }, {
            "email": "petra.pickles@example.org",
            "password": "Password123",
            "first_name": "Petra",
            "last_name": "Pickles",
            "role": "Administrator",
        }, {
            "email": "marty.major@example.org",
            "password": "Password123",
            "first_name": "Marty",
            "last_name": "Major",
            "role": "Director",
        }]

        for user in users:
            if User.objects.filter(**user).exists() == False:
                User.objects.create_user(**user)

    def add_terms(self):
        terms = [{
            "order": 1,
            "start_date": datetime(2022, 9, 1),
            "end_date": datetime(2022, 10, 21)
        }, {
            "order": 2,
            "start_date": datetime(2022, 10, 31),
            "end_date": datetime(2022, 12, 16)
        }, {
            "order": 3,
            "start_date": datetime(2023, 1, 3),
            "end_date": datetime(2023, 2, 10)
        }, {
            "order": 4,
            "start_date": datetime(2023, 2, 20),
            "end_date": datetime(2023, 3, 31)
        }, {
            "order": 5,
            "start_date": datetime(2023, 4, 17),
            "end_date": datetime(2023, 5, 26)
        }, {
            "order": 6,
            "start_date": datetime(2023, 6, 5),
            "end_date": datetime(2023, 7, 21)
        }]

        for term in terms:
            if Term.objects.filter(**term).exists() == False:
                Term.objects.create(**term)

    def handle(self, *args, **options):
        print("Seeding initial data...")
        try:
            self.add_users()
            self.add_terms()
            print("Data was seeded.")
        except:
            raise CommandError("Unable to seed data.")