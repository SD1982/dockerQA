#!/bin/bash

cd html || return

git clone https://github.com/PrestaShop/PrestaShop.git "${2}"
cd "${2}" || return
git checkout "${1}"
rm -rf * && git checkout . && composer install
git clean -xfd
make

$SHELL

