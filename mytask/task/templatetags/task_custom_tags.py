from django import template
register = template.Library()
from ..models import Task
from mytask.setup.models import Task_Status

@register.simple_tag
def totaltasks():
    return Task.objects.all().count()

@register.simple_tag
def completedtasks():
    return Task.objects.filter(status__code='Completed').count()

@register.simple_tag
def onholdtasks():
    return Task.objects.filter(status__code='On Hold').count()

@register.simple_tag
def cancelledtasks():
    return Task.objects.filter(status__code='Cancelled').count()

@register.simple_tag
def inprogresstasks():
    return Task.objects.filter(status__code='In Progress').count()

'''
Django offers a powerful way to follow relationships in lookups, taking care of the SQL JOINs automatically behind the scenes.
To span the relationships, use the field name of the the related fields accross the models, separated by double underscores,
until you get to the field you want.
'''
