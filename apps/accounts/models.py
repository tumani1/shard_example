# coding: utf-8

from django.db import models

#############################################################################################################
# Таблица
class Accounts(models.Model):
    name = models.CharField(verbose_name="Имя пользователя", max_length=100)

    def __unicode__(self):
        return u'[%s] %s' % (self.pk, self.name)

    # class Meta:
    #     # Имя таблицы в БД
    #     db_table = 'accounts'
    #     verbose_name = u'Пользователь'
    #     verbose_name_plural = u'Пользователи'
