#!/bin/bash

# Prefer US English and use UTF-8
export LC_ALL="en_US.UTF-8"
export LANG="en_US"
export DOTFILES="$HOME/Github/dotfiles"
export DF_SETTINGS="$DOTFILES/.settings"
export DF_CREDENTIALS="$DF_SETTINGS/credentials.json"
export DF_MACHINES="$DF_SETTINGS/machines.json"
export DF_DATABASES="$DF_SETTINGS/databases.json"
export DF_GITHUB="$DF_GITHUB/github.json"
export NUCLEUS="$HOME/Nucleus"


function source_lib () {
    d="$1"
    for f in $DOTFILES/.lib/*
    do
        if [ -f "$f" ]; then
            echo "[INFO] ... Sourcing $f"
            source $f # . $f
            echo "       ... OK "
        fi
    done
}

source_lib
