from django import template
from django.db.models import Sum, Avg, Max, Min, Count

register = template.Library()


@register.filter
def total_minutes(queryset):
    return queryset.aggregate(Sum('duration')).get('duration__sum')
@register.filter(name="range1")
def range1(max,min=1):
	return range(min,max)
@register.filter(name="sub")
def sub(value,args):
	return value - args
@register.filter(name="divide")
def divide(value,total=100):
	print(value)
	return total//value