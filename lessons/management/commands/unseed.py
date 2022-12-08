from django.core.management.base import BaseCommand, CommandError

from lessons.models import Invoice, Lesson, LessonRequest, Teacher, Term, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Unseeding initial data...")

        try:
            User.objects.filter(is_superuser=False).delete()
            Term.objects.all().delete()
            LessonRequest.objects.all().delete()
            Invoice.objects.all().delete()
            Teacher.objects.all().delete()
            Lesson.objects.all().delete()
        except:
            raise CommandError("Unable to unseed initial data.")

        print("Initial data unseeded.")
