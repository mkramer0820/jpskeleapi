from django.views.generic import DetailView, CreateView, UpdateView
from .models import SampleApprovalByBuyer
from task.NonApiView.forms import UpdateTaskForm, CreateTemplateTaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class CreateTemplateTaskView(CreateView):

    template_name = 'task/template_task_add.html'
    model = SampleApprovalByBuyer
    form_class = CreateTemplateTaskForm

    def form_valid(self, form):

        TemplateTask = form.save(commit=False)
        TemplateTask.save()

        return HttpResponseRedirect(reverse('index'))


class UpdateTaskView(UpdateView):

    form_class = UpdateTaskForm
    model = SampleApprovalByBuyer
    template_name = 'task/task_update_form.html'
    success_url = '/task/'


class OrderTaskDetail(DetailView):

    Model = SampleApprovalByBuyer
    context_object_name = 'open_tasks'
    queryset = SampleApprovalByBuyer.objects.all()
    template_name = 'task/task_detail.html'




#not used due to api view
"""
class OrderTaskList(ListView):

    model = SampleApprovalByBuyer
    context_object_name = 'task_list'
    template_name = 'task/task_list.html'
"""