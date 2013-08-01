# coding: utf-8

from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.settings import *
from apps.accounts.forms import *
from apps.accounts.models import *


def index(request):
    resp_dict = {}
    context = RequestContext(request)

    if request.method == 'POST':
        form = AccountForm(request.POST, initial=request.POST)
        if form.is_valid():
            form.save()

            messages.info(request, u'Данные сохранены!')
            return HttpResponseRedirect(request.path)

        else:
            messages.error(request, u'Форма содержит ошибки!')
    else:
        # Инициализация
        form = AccountForm(initial={})

    resp_dict['form'] = form

    # Пагинация
    o_account = Accounts.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(o_account, APP_ITEM_PER_PAGE)

    try:
        p_page = paginator.page(page)
    except PageNotAnInteger:
        p_page = paginator.page(1)
    except EmptyPage:
        p_page = paginator.page(paginator.num_pages)

    resp_dict['paging'] = p_page
    return render_to_response('account/index.html', resp_dict, context_instance=context)
