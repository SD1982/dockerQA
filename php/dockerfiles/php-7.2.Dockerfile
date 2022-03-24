FROM php:7.2-apache

ENV DEBIAN_FRONTEND=nointeractive
ENV NODE_VERSION=14.x

ARG APP_UID
ARG APP_GID

# Install dependencies
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
  curl \
  git \
  zip unzip \
  apt-utils \
  mailutils

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | sudo bash - && \
    apt-get install -y nodejs

# Install extensions
ADD scripts/installPhpExt.sh /root/installPhpExt.sh
RUN chmod uga+x /root/installPhpExt.sh && sync
RUN /root/installPhpExt.sh

RUN a2enmod rewrite
RUN groupmod -g $APP_GID www-data && usermod -u $APP_UID -g $APP_GID www-data
RUN chown -R $APP_UID:$APP_GID /var/www
