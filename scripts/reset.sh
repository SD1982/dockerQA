#!/bin/bash

cd html/"${1}" || return

git reset --hard
git checkout "${2}"
rm -rf * && git checkout . && composer install
git clean -xfd
make install
git st

$SHELL