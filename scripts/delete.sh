#!/bin/bash

cd html || return

rm -rf "${1}" || return

$SHELL