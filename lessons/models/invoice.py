from django.db import models

#Create Invoices, for the user and for which lesson
class Invoice(models.Model):
    lesson_request = models.ForeignKey("lessons.LessonRequest", on_delete=models.CASCADE)
    user = models.ForeignKey("lessons.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"#{str(self.user.pk).zfill(4)}-{str(self.pk).zfill(3)}"
