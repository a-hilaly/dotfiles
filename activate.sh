#!/bin/bash


export DOTFILES="$HOME/Github/dotfiles"
export DOTFILES_CONFIGURATIONS="$DOTFILES/df.configs"
export CRED_CONF="$DOTFILES_CONFIGURATIONS/cred.config.json"
export NUCLEUS="$HOME/Nucleus"

export PATH=$PATH:$HOME/go/bin

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
