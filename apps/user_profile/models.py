# coding: utf-8

from django.db import models

from apps.accounts.models import *


#############################################################################################################
# Таблица пользователей
class UserProfile(models.Model):
    user   = models.IntegerField(verbose_name="Пользователь")
    email  = models.EmailField(verbose_name="E-mail")
    adress = models.CharField(verbose_name="Адресс", max_length = 100)

    def __unicode__(self):
        return u'[%s]' % (self.pk)

    # class Meta:
    #     # Имя таблицы в БД
    #     # db_table = 'user_profile'
    #     verbose_name = 'Профиль пользователя'
    #     verbose_name_plural = 'Профили пользователей'
