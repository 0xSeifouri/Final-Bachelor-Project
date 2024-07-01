from django import template

register = template.Library()

@register.filter
def persian_number(number):
    number = str(number)
    en_to_per = number.maketrans('0123456789', '۰١۲۳۴۵۶۷۸۹')
    return number.translate(en_to_per)