#!/bin/bash

function nginx_conf {
    # Nginx conf
    NGINX_AVAILABLE='/etc/nginx/sites-available'
    NGINX_ENABLED='/etc/nginx/sites-enabled'

    if [ ! -d $NGINX_AVAILABLE ]; then
        mkdir $NGINX_AVAILABLE
    fi

    if [ ! -d $NGINX_ENABLED ]; then
        mkdir $NGINX_ENABLED
    fi

    if [ ! -f $NGINX_AVAILABLE/my_information_nginx ]; then
        cp my_information_nginx $NGINX_AVAILABLE
        ln -s $NGINX_AVAILABLE/my_information_nginx $NGINX_ENABLED/my_information_nginx
    fi
}

function gunicorn_conf {
    cp gunicorn_start ../env/bin/
    chown webapp:nginx ../env/bin/gunicorn_start
}

function supervisord_config {
  if [ ! -f /etc/supervisord.d/my_information.conf ]; then
        cp my_information.conf /etc/supervisord.d/
        supervisorctl reload myinformation
    fi
}

function main {
nginx_conf
gunicorn_conf
supervisord_config
}