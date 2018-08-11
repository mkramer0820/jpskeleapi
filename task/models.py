from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from orders.models import Orders

note = models.CharField(blank=True, max_length=100)
date_field = models.DateField(blank=True)


class TaskType(models.Model):

    type = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.type


class StandardTaskList(models.Model):

    type = models.ForeignKey('TaskType', on_delete='CASCADE')
    created = models.DateTimeField(verbose_name='Create On', auto_now=True)
    due_date = models.DateField(null=True,blank=True)
    due_date_note = models.CharField(blank=True, max_length=100)
    factory_ta = models.DateField(null=True,blank=True)
    factory_ta_note = models.CharField(blank=True, max_length=100)
    date_sent_to_jp = models.DateField(null=True, blank=True)
    date_sent_to_jp_note = models.CharField(blank=True, max_length=100)
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


class SampleTaskBasic(StandardTaskList):

    order = models.ForeignKey(Orders, blank=True, on_delete='CASCADE')
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