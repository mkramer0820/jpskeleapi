from django.contrib import admin
from task.models import SampleTaskBasic, TaskType

admin.site.register(SampleTaskBasic)
admin.site.register(TaskType)