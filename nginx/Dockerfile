FROM nginx:1.23.2-alpine
RUN addgroup -g 1000 -S www-data \
 && adduser -u 1000 -D -S -G www-data www-data

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
