from django import template

register = template.Library()


@register.filter
def active_comments(comments):
    return comments.filter(active=True)

@register.filter
def order_comments(comments):
    return  comments.order_by('-datetime_created')
