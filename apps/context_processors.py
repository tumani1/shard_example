# coding: utf-8

from apps import settings

# Общий контекст
def context(request):
    context = {}

    # Массив с параметрами конфигурации
    proto = 'http'
    if request.is_secure(): proto = 'https'

    context['settings'] = settings
    context['protocol'] = proto

    return context
