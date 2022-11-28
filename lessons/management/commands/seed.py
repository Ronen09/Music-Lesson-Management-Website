from django.core.management.base import BaseCommand, CommandError

from lessons.models import User, Term, LessonRequest, Teacher, Lesson

from datetime import datetime
from django.utils import timezone


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
            if User.objects.filter(email=user["email"]).exists() == False:
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

    def add_lesson_requests(self):
        # Get John Doe (student)
        john_doe_user = User.objects.filter(
            email="john.doe@example.org").first()

        lesson_requests = [{
            "is_available_on_monday": True,
            "is_available_on_tuesday": True,
            "is_available_on_wednesday": False,
            "is_available_on_thursday": False,
            "is_available_on_friday": True,
            "no_of_lessons": 5,
            "lesson_interval_in_days": 7,
            "lesson_duration_in_mins": 45,
            "further_information": "I have learning difficulties.",
            "user": john_doe_user,
        }, {
            "is_available_on_monday": False,
            "is_available_on_tuesday": True,
            "is_available_on_wednesday": True,
            "is_available_on_thursday": True,
            "is_available_on_friday": True,
            "no_of_lessons": 4,
            "lesson_interval_in_days": 14,
            "lesson_duration_in_mins": 60,
            "is_fulfilled": True,
            "user": john_doe_user,
        }]

        for lesson_request in lesson_requests:
            if LessonRequest.objects.filter(
                    **lesson_request).exists() == False:
                LessonRequest.objects.create(**lesson_request)

    def add_teachers(self):
        teachers = [{
            "first_name": "John",
            "last_name": "Simmons"
        }, {
            "first_name": "Rebecca",
            "last_name": "Smith",
        }, {
            "first_name": "Daniel",
            "last_name": "Baker"
        }]

        for teacher in teachers:
            if Teacher.objects.filter(**teacher).exists() == False:
                Teacher.objects.create(**teacher)

    def add_lessons(self):
        john_doe_user = User.objects.filter(
            email="john.doe@example.org").first()
        john_doe_lesson_request = LessonRequest.objects.filter(
            user=john_doe_user).first()
        rebecca_smith_teacher = Teacher.objects.filter(
            first_name="Rebecca", last_name="Smith").first()

        lessons = [{
            "teacher": rebecca_smith_teacher,
            "datetime": datetime(2023, 5, 2, 13, 0, tzinfo=timezone.utc),
            "duration": 45,
            "further_information": "I want to learn piano.",
            "user": john_doe_user,
            "lesson_request": john_doe_lesson_request,
        }]

        for lesson in lessons:
            if Lesson.objects.filter(**lesson).exists() == False:
                Lesson.objects.create(**lesson)

    def handle(self, *args, **options):
        print("Seeding initial data...")

        #try:
        self.add_users()
        self.add_terms()
        self.add_lesson_requests()
        self.add_teachers()
        self.add_lessons()
        print("Data was seeded.")
        #except:
        #    raise CommandError("Unable to seed initial data.")