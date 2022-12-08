from django.views.generic.edit import CreateView

from lessons.forms import LessonCreateForm
from lessons.models import Lesson, LessonRequest


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonCreateForm
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator", "Director"],
        "dashboard": {
            "heading": "Create new lesson",
            "subheading": "Create a new lesson by specifying details."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"

    def get_initial(self):
        initial = super(AdministratorLessonCreateView, self).get_initial()

        lesson_request = LessonRequest.objects.filter(pk=self.kwargs["lesson_request_id"]).first()

        initial["lesson_request"] = lesson_request.pk
        initial["user"] = lesson_request.user.pk
        return initial