#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weiduadmin_sub.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


#run
#uwsgi --ini weiduadmin_sub.ini
#nohup nice -n 0 uwsgi --master --http :8000 --wsgi-file weiduadmin_sub/wsgi.py  --process 8 --listen=1024 --buffer-size=102400 --max-requests=4096 >/dev/null &
# [uwsgi]
# #sockert
# http=0.0.0.0:8000
#
# #project_dr
# chdir=/home/weiduadmin_sub
#
# #project_name
# module=weiduadmin_sub.wsgi
#
# master=true
#
# processes=16
#
# listen = 1024
#
# max-requests = 4096
#
# chmod-socket=666
#
# buffer-size=65536
#
# harakiri-verbose=true
# harakiri=300