FROM nginx:1.23.2-alpine

RUN rm /etc/nginx/conf.d/default.conf && \
    mkdir -p /var/www/artsya.co

COPY nginx/*.conf /etc/nginx/conf.d/
COPY web/ /var/www/artsya.co