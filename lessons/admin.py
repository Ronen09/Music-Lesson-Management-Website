from django.contrib import admin

from lessons.models import User, LessonRequest

# Register your models here.
admin.site.register(User)
admin.site.register(LessonRequest)
