#!/bin/sh

curl -sSLf \
  -o /usr/local/bin/install-php-extensions \
  https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions

chmod uga+x /usr/local/bin/install-php-extensions && sync

# Install php extensions
install-php-extensions \
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
install-php-extensions @composer-1
