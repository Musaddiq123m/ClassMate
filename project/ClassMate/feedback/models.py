from django.db import models
from user.models import Student
from django.utils import timezone
from section.models import Section

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=False)
    feedback_text = models.TextField()
    submission_date = models.DateTimeField(default=timezone.now)
    starred = models.BooleanField(default=False) 

    class Meta:
        unique_together = ('student', 'section', 'feedback_text')

    def __str__(self):
        return f"Feedback for {self.section} by {self.student.user.username}"
