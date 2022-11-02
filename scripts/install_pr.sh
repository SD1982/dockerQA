#!/bin/bash

cd html/"${1}"


git reset --hard
git checkout "${2}"
rm -rf * && git checkout . && composer install
git clean -xfd
git prc origin "${3}" "${2}"
make install
git st