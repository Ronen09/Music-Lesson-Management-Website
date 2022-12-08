from django.views.generic.edit import DeleteView

from lessons.models import User

class AdminDeleteView(DeleteView):
    model = User
    template_name = "delete.html"
    extra_context = {
        "allowed_roles": ["Director", "Administrator"],
        "dashboard": {
            "heading": "Delete this administrator account",
            "subheading": "Confirm deletion of this administrator account."
        }
    }

    def get_success_url(self):
        return f"/director/manage-administrators"
