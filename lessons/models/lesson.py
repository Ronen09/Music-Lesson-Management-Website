from django.db import models

from lessons.models import User, Teacher, LessonRequest

# Create the class Lesson with the correct attributes and datatypes
class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    datetime = models.DateTimeField()

    duration = models.IntegerField()
    # additional information section, set that completion is optional
    further_information = models.CharField(max_length=255,
                                           null=True,
                                           blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    lesson_request = models.ForeignKey(LessonRequest, on_delete=models.CASCADE)
    

    
