#!/bin/sh
export GPG_TTY=$(tty)
mkdir config
ls -la
gpg --quiet --batch --yes --decrypt --passphrase="$CONFIG_INI_PASSPHRASE" \
--output ./config/config.ini config.ini.gpg
ls -la ./config