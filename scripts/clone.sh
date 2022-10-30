#!/bin/bash

cd html

git clone https://github.com/PrestaShop/PrestaShop.git "${1}" && \
    cd "${1}" && \
    git checkout "${2}" && \
    rm -rf --* && git checkout . && composer install && \
    git clean -xfd && \
    make