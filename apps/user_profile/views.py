# coding: utf-8

from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.settings import *
from apps.user_profile.forms import *
from apps.user_profile.models import *
from apps.accounts.models import *
from apps.common.util import *


def index(request):
    resp_dict = {}
    context = RequestContext(request)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, initial=request.POST)
        if form.is_valid():
            result = form.save()

            if result:
                messages.info(request, u'Данные сохранены!')
                return HttpResponseRedirect(request.path)
            else:
                messages.error(request, u'Не удалось сохранить!')
        else:
            messages.error(request, u'Форма содержит ошибки!')
    else:
        data = {}
        form = UserProfileForm(initial=data)

    resp_dict['form'] = form
    return render_to_response('user_profile/index.html', resp_dict, context_instance=context)

def get_shard_values(request, name=None):
    resp_dict = {}
    context = RequestContext(request)

    if not name is None:
        if name in APP_SHARD_PROFILE:
            # Пагинация
            o_profile = UserProfile.objects.using(name).all()

            page = request.GET.get('page', 1)
            paginator = Paginator(o_profile, APP_ITEM_PER_PAGE)

            try:
                p_page = paginator.page(page)
            except PageNotAnInteger:
                p_page = paginator.page(1)
            except EmptyPage:
                p_page = paginator.page(paginator.num_pages)

            list_profile = reindex_by(p_page.object_list, 'user', True)
            if len(list_profile):
                o_accunts = Accounts.objects.filter(pk__in=list_profile.keys())
                list_account = reindex_by(o_accunts, 'pk', True)
                resp_dict['account'] = list_account

            resp_dict['paging'] = p_page
        else:
            messages.error(request, u"Шарда с таким ID:'%s' не найдено!" % (name))


    return render_to_response('user_profile/shard_value.html', resp_dict, context_instance=context)
