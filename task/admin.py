from django.contrib import admin
from task.models import CostcoSampleTasks, TaskType, Task, TaskName


admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(CostcoSampleTasks)
admin.site.register(TaskName)