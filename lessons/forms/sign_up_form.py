from django import forms

from lessons.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]

    new_password = forms.CharField(label="New password", widget=forms.PasswordInput())

    password_confirmation = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput()
    )

    def clean(self):
        super().clean()

        new_password = self.cleaned_data.get("new_password")
        password_confirmation = self.cleaned_data.get("password_confirmation")

        if new_password != password_confirmation:
            self.add_error(
                "password_confirmation", "Confirmation does not match password."
            )

    def save(self, commit=True):
        super().save(commit=False)

        user = User.objects.create_user(
            self.cleaned_data.get("email"),
            password=self.cleaned_data.get("new_password"),
        )

        return user
