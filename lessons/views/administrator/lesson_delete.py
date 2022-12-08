from django.views.generic.edit import DeleteView

from lessons.models import Lesson


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = "delete.html"
    extra_context = {
        "allowed_roles": ["Administrator", "Director"],
        "dashboard": {
            "heading": "Delete lesson",
            "subheading": "Confirm deletion of lesson."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"