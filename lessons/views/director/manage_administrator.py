from django.shortcuts import render
from django.urls import reverse

from lessons.forms.administrator import LessonRequestsFilterForm
from lessons.models import User, UserManager

def administrator_list(request):
    # Get form
    if request.method == "POST":
        form = LessonRequestsFilterForm(request.POST)
    else:
        form = LessonRequestsFilterForm()

    # Generate correct list of requests to show
    administrators = User.objects.filter(role="Administrator")

    def convert_administrators_to_card(administrator):
        heading = administrator.email
        first_name = administrator.first_name
        last_name = administrator.last_name

        return {
            "heading":
                heading,
            "info": [{
                "title": "First Name",
                "description": first_name,
            }, {
                "title": "Last Name",
                "description": last_name,
            }],
#            "buttons": [{
#                "name": "Edit",
#                "url": edit_url,
#                "type": "outline-primary",
#            }, {
#                "name": "Delete",
#                "url": delete_url,
#                "type": "outline-danger",
#            }],
        }

    cards = map(convert_administrators_to_card, administrators)
    # Return page
    return render(
        request, "director/manage_administrators.html", {
            "allowed_roles": ["Director"],
            "administrators": administrators,
            "dashboard": {
                "heading": "Administrators",
                "subheading": "Manage administrators."
            },
            "cards": cards
        })
