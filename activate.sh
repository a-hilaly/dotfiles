#!/bin/bash

export DOTFILES="$HOME/Github/dotfiles"
export DOTFILES_CONFIGURATIONS="$DOTFILES/df.config"
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
