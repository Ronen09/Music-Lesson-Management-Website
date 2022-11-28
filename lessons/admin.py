from django.contrib import admin

from lessons.models import User, LessonRequest, Term, Teacher, Lesson

# Register your models here.
admin.site.register(User)
admin.site.register(LessonRequest)
admin.site.register(Term)
admin.site.register(Teacher)
admin.site.register(Lesson)