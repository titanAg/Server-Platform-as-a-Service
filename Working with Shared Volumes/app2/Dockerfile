FROM postgres:alpine
RUN apk add python3
RUN apk add py3-gunicorn
COPY app.py /var/www/app.py
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 --chdir /var/www/ app:app