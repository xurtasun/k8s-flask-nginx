FROM nginx:latest

RUN mkdir /data && mkdir /data/nginx/ && touch /data/nginx/cache

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80/tcp

