FROM postgres:alpine

RUN apk update
RUN apk add python3
RUN apk add py3-gunicorn
RUN apk add py3-pip
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install psycopg2

RUN mkdir /var/www
RUN mkdir /var/www/pgsql

COPY webapp.py /var/www/webapp.py
COPY landing.html /var/www/landing.html
COPY scheduledjob.py /var/www/scheduledjob.py
COPY cronjob.txt /var/www/cronjob.txt
COPY startup.sh /var/www/startup.sh

RUN chmod +x /var/www/startup.sh
RUN chown postgres -R /var/www

EXPOSE 80
CMD ["./var/www/startup.sh"]