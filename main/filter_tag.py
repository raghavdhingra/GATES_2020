from django import template

register = template.Library()

@register.filter(name='timing')
def timing(value):
    arr = value.split(":")
    arr1 = arr[2].split(" ")
    val = "{}:{} {}".format(arr[0],arr[1],arr1[1])
    return val