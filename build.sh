#!/bin/bash

# Get the UID & GID and write in .Dockerfile files
# shellcheck disable=SC2116
# shellcheck disable=SC2046
# shellcheck disable=SC2005
echo "$(echo "RUN groupmod -g ")""$(echo $(id -g))""$(echo " www-data && usermod -u ")""$(echo $(id -u))""$(echo " -g ")""$(echo $(id -g))""$(echo " www-data")" >> ./php/dockerfiles/php-7.1.Dockerfile
echo "$(echo "RUN chown -R ")""$(echo $(id -u))""$(echo ":")""$(echo $(id -g))""$(echo " /var/www")" >> ./php/dockerfiles/php-7.1.Dockerfile

echo "$(echo "RUN groupmod -g ")""$(echo $(id -g))""$(echo " www-data && usermod -u ")""$(echo $(id -u))""$(echo " -g ")""$(echo $(id -g))""$(echo " www-data")" >> ./php/dockerfiles/php-7.2.Dockerfile
echo "$(echo "RUN chown -R ")""$(echo $(id -u))""$(echo ":")""$(echo $(id -g))""$(echo " /var/www")" >> ./php/dockerfiles/php-7.2.Dockerfile

echo "$(echo "RUN groupmod -g ")""$(echo $(id -g))""$(echo " www-data && usermod -u ")""$(echo $(id -u))""$(echo " -g ")""$(echo $(id -g))""$(echo " www-data")" >> ./php/dockerfiles/php-7.3.Dockerfile
echo "$(echo "RUN chown -R ")""$(echo $(id -u))""$(echo ":")""$(echo $(id -g))""$(echo " /var/www")" >> ./php/dockerfiles/php-7.3.Dockerfile

echo "$(echo "RUN groupmod -g ")""$(echo $(id -g))""$(echo " www-data && usermod -u ")""$(echo $(id -u))""$(echo " -g ")""$(echo $(id -g))""$(echo " www-data")" >> ./php/dockerfiles/php-7.4.Dockerfile
echo "$(echo "RUN chown -R ")""$(echo $(id -u))""$(echo ":")""$(echo $(id -g))""$(echo " /var/www")" >> ./php/dockerfiles/php-7.4.Dockerfile

# Start build
docker-compose up
