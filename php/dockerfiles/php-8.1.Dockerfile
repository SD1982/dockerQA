FROM php:8.1-apache

ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod uga+x /usr/local/bin/install-php-extensions && sync

ENV DEBIAN_FRONTEND=nointeractive

ARG APP_UID
ARG APP_GID

# Install dependencies
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
  curl \
  git \
  nodejs \
  zip unzip \
  apt-utils mailutils

# Install extensions
RUN install-php-extensions \
  bcmath \
  bz2 \
  calendar \
  imap \
  exif \
  gd \
  intl \
  ldap \
  memcached \
  mysqli \
  opcache \
  pdo_mysql \
  pdo_pgsql \
  pgsql \
  redis \
  soap \
  xsl \
  zip \
  xdebug \
  sockets

# Install composer
RUN install-php-extensions @composer-1

RUN a2enmod rewrite
RUN groupmod -g $APP_GID www-data && usermod -u $APP_UID -g $APP_GID www-data
RUN chown -R $APP_UID:$APP_GID /var/www
