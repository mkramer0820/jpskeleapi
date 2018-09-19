from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from orders.models import Orders
from django.contrib.postgres.fields import JSONField

note = models.CharField(blank=True, max_length=100)
date_field = models.DateField(blank=True)


class TaskType(models.Model):

    type = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.type


class TaskName(models.Model):
    type = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.type

class CostcoSampleTaskAbstract(models.Model):

    type = models.ForeignKey('TaskType', on_delete='CASCADE')
    created = models.DateTimeField(verbose_name='Create On', auto_now=True)
    due_date = models.DateField(null=True,blank=True)
    due_date_factory_ta = models.DateField(null=True,blank=True)
    jp_approval_sent_to_buyer = models.DateField(null=True, blank=True)

    buyer_approval_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=(('In progress', 'in_progress'),
                                       ('Completed', 'completed'),
                                       ('Cancelled', 'cancelled')),
                              blank=True, max_length=20)
    standard_task_note = models.TextField(blank=True, null=True, verbose_name="General Notes")

    def __str__(self):
        return self.type

    class Meta:

        abstract = True


class CostcoSampleTasks(CostcoSampleTaskAbstract):

    order = models.ForeignKey(Orders, blank=True, on_delete='CASCADE')
    name = models.OneToOneField(TaskName, on_delete='CASCADE')
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s - %s" %(self.order, self.type)

    def save(self, *args, **kwargs):
        slug1 = slugify(self.order.buyer_style_number)
        slug2 = slugify(self.type)
        slug = slug1+" "+slug2
        self.slug = slugify(slug)
        super(SampleTaskBasic, self).save(*args,**kwargs)

    def get_absolute_url(self):

        return reverse('task:task_detail',  kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('task:update_task', kwargs={'slug':self.slug})

    @property
    def style_number(self):

        return "%s" % (self.order.buyer_style_number)

def defualtTaskAttribute():

    return {'task_name': '', 'task_due_date': '', 'task_note':''}


class Task(models.Model):

    task_name = models.CharField
    task_data = JSONField(default=defualtTaskAttribute())
    task_order = models.ForeignKey(Orders, on_delete='CASCADE')

    def __str__(self):
        return self.task_name