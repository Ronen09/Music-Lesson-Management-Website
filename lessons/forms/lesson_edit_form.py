from django import forms

from lessons.models import Lesson


class LessonEditForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ("datetime", "teacher", "duration", "further_information",
                  "user", "lesson_request")
        widgets = {
            "datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "user": forms.HiddenInput(),
            "lesson_request": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(LessonEditForm, self).__init__(*args, **kwargs)
        self.fields["duration"].widget.attrs["placeholder"] = "e.g. 45 minutes"