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


class SubStage(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Block(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    title = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Level(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BlockInventory(models.Model):
    inventory = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)


class ProgressEntry(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BlockProgress(models.Model): pass
