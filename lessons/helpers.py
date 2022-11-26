from lessons.models import User, Term


def get_students():
    return User.objects.all().filter(role="Student", is_superuser=False)


def get_terms():
    return Term.objects.all()