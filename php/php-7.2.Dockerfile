FROM php:7.2-apache

RUN apt-get update
RUN apt-get upgrade -y

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN chmod uga+x /usr/local/bin/install-php-extensions && sync

RUN DEBIAN_FRONTEND=nointeractive apt-get update -q \
    && DEBIAN_FRONTEND=nointeractive apt-get install -qq -y \
        curl \
        git \
        zip unzip \
    && install-php-extensions \
        bcmath \
        bz2 \
        calendar \
        curl \
        date \
        dom \
        fileinfo \
        filter \
        ftp \
        hash \
        iconv \
        imap \
        json \
        libxml \
        mbstring \
        openssl \
        session \
        xmlreader \
        xmlwriter \
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
        xml \
        xdebug \
        sockets

RUN a2enmod rewrite
RUN groupmod -g 1000 www-data \
  && usermod -u 1000 -g 1000 www-data
RUN chown -R 1000:1000 /var/www