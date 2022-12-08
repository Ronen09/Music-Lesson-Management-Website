from django.views.generic.edit import UpdateView

from lessons.forms import LessonEditForm
from lessons.models import Lesson

# Class for updating Lesson View
class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonEditForm
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator", "Director"],
        "dashboard": {
            "heading": "Modify lesson",
            "subheading": "Change details about this lesson."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"
