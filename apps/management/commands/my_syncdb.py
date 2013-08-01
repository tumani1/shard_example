# coding: utf-8

import sys
import traceback
import subprocess
from optparse import make_option

from django.core.management.base import NoArgsCommand, CommandError

import apps
from apps.settings import DATABASES


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('-u', '--username',
            action  = 'store_true',
            dest    = 'username',
            default = False,
            help    = 'Create superuser',
        ),
    )

    help = 'My syncdb command for task'
    requires_model_validation = True

    def handle_noargs(self, **options):
        print "=============== Dropping databases ==============="
        for k,v in DATABASES.items():
             if 'NAME' in v:
                 subprocess.call('mysql -u%s -e "drop database %s"' % (v['USER'], v['NAME']), shell=True)

        print "=============== Creating databases ==============="
        for k,v in DATABASES.items():
            if 'NAME' in v:
                subprocess.call('mysql -u%s -e "create database %s"' % (v['USER'], v['NAME']), shell=True)

        for i in DATABASES.keys():
            print "=============== syncing %s ===============" % (i)
            subprocess.call('python manage.py syncdb --noinput --database=%s' % (i), shell=True)

        if options.get('username', False):
            print "Creating superuser"
            subprocess.call('python manage.py createsuperuser --username=admin --email=admin@example.com', shell=True)

        return False

def traceback_own(excpt):
    err_l = 'Error'
    if excpt.__class__.__name__ == 'KeyError':
        err_l = 'KeyError'

    exc_type, exc_value, exc_traceback = sys.exc_info()
    trace_msg = ''.join(traceback.format_tb(exc_traceback))

    print '============================='
    print '%s: %s' % (err_l, excpt)
    print '============================='
    print 'Traceback:\n%s' % trace_msg
    print '============================='
