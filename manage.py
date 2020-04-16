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

#nginx http转发
# upstream weiduadmin_sub_88{
#     server 127.0.0.1:88;
# }
#
# server {
#     listen       80;
#     server_name  sub.assess.admin.iwedoing.com;
#     access_log logs/weiduadmin_sub_88.log;
#     error_log logs/weiduadmin_sub_88.error;
#
#     location / {
#         proxy_set_header Host $host;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_pass http://weiduadmin_sub_88;
#     }
# }

#nginx uwsgi转发
# server {
#         listen       80;
#         server_name  sub.assess.admin.iwedoing.com;
#
#         add_header Vary "Accept-Encoding, User-Agent";
#
#         charset utf-8;
#         error_log  logs/admin_sub.error.log;
#         access_log  logs/admin_sub.access.log  main;
#
#
#         location / {
#                 uwsgi_pass wdadmin_sub_uwsgi;
#                 include uwsgi_params;
#                 uwsgi_connect_timeout 1800;
#                 uwsgi_read_timeout 1800;
#                 uwsgi_send_timeout 1800;
#                 proxy_read_timeout 1800;
#         }
#
#         error_page   500 502 503 504  /50x.html;
#         location = /50x.html {
#                 root   html;
#         }
#
# }
