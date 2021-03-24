FROM php:7.3-apache

RUN apt-get update
RUN apt-get upgrade -y

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN chmod uga+x /usr/local/bin/install-php-extensions && sync

ENV DEBIAN_FRONTEND=nointeractive

# Install dependencies
RUN  apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
  curl \
  git \
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
RUN groupmod -g 1000 www-data \
  && usermod -u 1000 -g 1000 www-data
RUN chown -R 1000:1000 /var/www