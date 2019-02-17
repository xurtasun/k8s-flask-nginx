FROM tiangolo/uwsgi-nginx-flask:python2.7

RUN pip install pytz

COPY ./app/main.py /app/main.py
COPY ./nginx/conf/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/conf/conf.d/nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 80/tcp

