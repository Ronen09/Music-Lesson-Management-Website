from django.db import models


class Invoice(models.Model):
    lesson_request = models.ForeignKey("lessons.LessonRequest", on_delete=models.CASCADE)
    user = models.ForeignKey("lessons.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.pk}-{self.pk}"