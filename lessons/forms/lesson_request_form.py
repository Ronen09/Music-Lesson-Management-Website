from django import forms

from lessons.models import LessonRequest


class LessonRequestForm(forms.ModelForm):
    class Meta:
        model = LessonRequest
        fields = [
            "is_available_on_monday",
            "is_available_on_tuesday",
            "is_available_on_wednesday",
            "is_available_on_thursday",
            "is_available_on_friday",
            "no_of_lessons",
            "lesson_interval_in_days",
            "lesson_duration_in_mins",
            "further_information",
        ]
