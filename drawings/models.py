from django.db import models

from user.models import User
from project_management.models import Project


# Drawings
class Plans(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PlanOption(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Drawing(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_option = models.ForeignKey(PlanOption, on_delete=models.CASCADE)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    drawing = models.FileField()

    def __str__(self):
        return self.parent_option.title


class DrawingRemark(models.Model):
    remarked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.drawing.id
