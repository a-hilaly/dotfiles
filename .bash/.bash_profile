#!/bin/bash

# Prefer US English and use UTF-8
export LC_ALL="en_US.UTF-8"
export LANG="en_US"
export DOTFILES="$HOME/Github/dotfiles"
export DOTFILES_CONFIGURATIONS="$DOTFILES/df.config"
export NUCLEUS="$HOME/Nucleus"


function source_lib () {
    d="$1"
    for f in $DOTFILES/.src/*
    do
        if [ -f "$f" ]; then
            echo "[INFO] ... Sourcing $f"
            source $f # . $f
            echo "       ... OK "
        fi
    done
}

source_lib
