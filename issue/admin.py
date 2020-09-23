from django.contrib import admin
from issue.models import Issue, IssueImage, IssueRemark, Notification, ProgressEntries

# Register your models here.

admin.site.register(Issue)
admin.site.register(IssueImage)
admin.site.register(IssueRemark)
admin.site.register(Notification)
admin.site.register(ProgressEntries)