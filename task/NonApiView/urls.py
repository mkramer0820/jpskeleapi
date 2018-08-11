from django.conf.urls import url
from .views import OrderTaskDetail,  CreateTemplateTaskView, UpdateTaskView
from .serializers import TemplateTaskList
"""OrderTaskList"""
app_name = 'task'

urlpatterns = [
    url(r'^add/$', CreateTemplateTaskView.as_view(), name='add_task'),
    url(r'^slug/update/(?P<slug>[-\w]+)/$', UpdateTaskView.as_view(), name='update_task'),

    url(r'^$', TemplateTaskList.as_view(), name='tasklist'),
    url(r'(?P<slug>[-\w]+)/$', OrderTaskDetail.as_view(), name='task_detail'),
    # url(r'^$', OrderList.as_view(), name='orderlist'),
    # url(r'(?P<pk>\w+)/$', OrderDetails.as_view(), name='order_details'),
    # url(r'^api/$', OrderReadView.as_view(), name='order_rest_api'),

]


"""
useful regex urls
pk (?P<pk>\d+)
slug : (?P<slug>[-\w]+)
slug + pk (?P<slug>[-\w]+)-(?P<pk>\d+)
(?P<username>[\w.@+-]+)

dates = (?P<year>[0-9]{4})
year mont  = (?P<year>[0-9]{4})/(?P<month>[0-9]{2})
ymd (?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})

"""
