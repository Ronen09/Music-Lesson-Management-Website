from django.core.validators import MinValueValidator
from django.db import models

from lessons.models import User

# Creates LessonRequest class, allowing users to set their availability for the weekdays
# Set to default True
class LessonRequest(models.Model):
    is_available_on_monday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_tuesday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_wednesday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_thursday = models.BooleanField(null=True, blank=True, default=True)
    is_available_on_friday = models.BooleanField(null=True, blank=True, default=True)
    
    # Creates number of leessons, intervals and the duration
    no_of_lessons = models.IntegerField(validators=[MinValueValidator(1)])
    lesson_interval_in_days = models.IntegerField(validators=[MinValueValidator(1)])
    lesson_duration_in_mins = models.IntegerField(validators=[MinValueValidator(1)])
    
    # additional information section, allows users to keep empty if not needed
    further_information = models.CharField(max_length=255, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_fulfilled = models.BooleanField(default=False)
