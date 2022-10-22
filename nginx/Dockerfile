FROM nginx:1.23.2-alpine
RUN addgroup -g 1000 -S www-user
RUN adduser -u 1000 -D -S -G www-user www-user

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
