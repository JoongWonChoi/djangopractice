from django import template

register = template.Library()

#애너테이션 적용하여 탬플릿에서 함수 사용하기

@register.filter
def sub(value,arg):
    return value-arg