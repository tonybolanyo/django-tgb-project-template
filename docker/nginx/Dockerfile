FROM nginx:1.17.2-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.global.conf /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/conf.d