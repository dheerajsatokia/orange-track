from django.db import models

from inventory.models import InventoryItem
from project_management.models import Project
from site_manage.models import Site


# Stages
class Stage(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class SubStage(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class SubStageInventory(models.Model):
    sub_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)


class Block(models.Model):
    sub_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Level(models.Model):
    title = models.CharField(max_length=255)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class ProgressEntry(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.block.title}"


class ProgressInventoryEntry(models.Model):
    progress_entry = models.ForeignKey(ProgressEntry, on_delete=models.CASCADE)
    inventory = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.inventory.name}"


class ProgressEntryMedia(models.Model):
    media = models.ImageField()
    progress_entry = models.ForeignKey(ProgressEntry, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.progress_entry.id}"


class ProgressComment(models.Model):
    comment = models.TextField()
    progress_entry = models.ForeignKey(ProgressEntry, on_delete=models.CASCADE)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.progress_entry.id}"
