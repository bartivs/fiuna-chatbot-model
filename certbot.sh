#!/bin/bash
certonly --reinstall --webroot --webroot-path=/var/www/certbot \
            --email ${EMAIL} --agree-tos --no-eff-email \
            -d ${BASE_URL}