#!/bin/sh
su postgres -c 'initdb /var/www/pgsql'
su postgres -c 'pg_ctl start -D /var/www/pgsql'
su postgres -c 'psql -c "create database test"'
crond -b -S
crontab /var/www/cronjob.txt
su postgres -c 'gunicorn --bind 0.0.0.0:80 --chdir /var/www webapp:app' 