# coding: utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    resp_dict = {}
    context = RequestContext(request)

    return render_to_response('base.html', resp_dict, context_instance=context)
