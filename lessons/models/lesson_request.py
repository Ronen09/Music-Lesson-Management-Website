from django.db import models


class LessonRequest(models.Model):
    is_available_on_monday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_tuesday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_wednesday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_thursday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_friday = models.BooleanField(null=True, blank=True, default=True)

    no_of_lessons = models.IntegerField()
    lesson_interval_in_days = models.IntegerField()
    lesson_duration_in_mins = models.IntegerField()

    further_information = models.CharField(max_length=255, null=True, blank=True)
