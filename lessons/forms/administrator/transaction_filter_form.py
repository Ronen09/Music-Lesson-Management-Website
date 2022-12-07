from django import forms

from lessons.models import User


class TransactionFilterForm(forms.Form):
    """A form used to filter transactions by a single selected student."""
    student_filter = forms.ModelChoiceField(label="Filter by student:",
                                            queryset=User.objects.filter(role="Student", is_superuser=False),
                                            empty_label="All",
                                            required=False)