# coding: utf-8

from django import template

register = template.Library()

@register.filter(name='dict_get')
def dict_get(map, key):
    try:
        return map[key]
    except:
        pass

    try:
        return map[str(key)]
    except:
        pass

    try:
        return getattr(map, key)()
    except:
        pass

    try:
        return getattr(map, key)
    except:
        pass

    return ''

def value_for_key(map, key):
    if key in map:
        resp = {
            'val':map[key]
        }
    else:
        resp = {
            'val':''
        }
    return resp

register.inclusion_tag('tmpl_tags/value_for_key.html')(value_for_key)
