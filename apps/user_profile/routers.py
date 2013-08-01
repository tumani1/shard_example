# coding: utf-8

from apps.settings import APP_SHARD_PROFILE

#############################################################################################################
# Маршрутизация
class UserProfileRouter(object):
    def db_for_read(self, model, **hints):
        return None

    def db_for_write(self, model, **hints):
        shard = None
        if model._meta.app_label == 'user_profile':
            if 'instance' in hints and hints['instance']:
                for k,v in APP_SHARD_PROFILE.items():
                    i1, i2 = v
                    if i1 <= hints['instance'].user <= i2:
                        shard = k
                        break

        return shard

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_syncdb(self, db, model):
        if db.startswith('shard'):
            return model._meta.app_label == 'user_profile'
        elif model._meta.app_label == 'user_profile':
            return False
        return None
